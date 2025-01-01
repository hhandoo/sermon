#include <iostream>
#include <vector>
#include <cstdlib>
#include <string>
#include <stdexcept>
#include <memory>
#include <array>
#include <regex>
namespace InternetCheck
{
    void logMessage(const std::string &message)
    {
        std::cout << message << std::endl;
    }
    void validateInputs(const std::vector<std::string> &sites, int timeoutInSeconds)
    {
        if (sites.empty())
        {
            throw std::invalid_argument("The list of sites cannot be empty.");
        }

        if (timeoutInSeconds <= 0)
        {
            throw std::invalid_argument("Timeout must be a positive integer.");
        }
    }
    bool checkInternetConnectivity(const std::vector<std::string> &sites, int timeoutInSeconds)
    {
        validateInputs(sites, timeoutInSeconds);

        bool isConnected = false;

        for (const auto &sitename : sites)
        {
            std::string command = "timeout " + std::to_string(timeoutInSeconds) +
                                  " ping -c 1 -W 1 " + sitename + " > /dev/null 2>&1";

            logMessage("Pinging: " + sitename + " | Command: " + command);

            int exitCode = system(command.c_str());
            if (exitCode == 0)
            {
                logMessage("Successfully pinged: " + sitename);
                isConnected = true;
            }
            else
            {
                logMessage("Failed to ping: " + sitename);
            }
        }

        return isConnected;
    }
    std::string exec(const char *cmd)
    {
        std::array<char, 128> buffer;
        std::string result;

        // Open the command using popen
        std::unique_ptr<FILE, int (*)(FILE *)> pipe(popen(cmd, "r"), pclose);
        if (!pipe)
        {
            throw std::runtime_error("popen failed!");
        }

        while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr)
        {
            result += buffer.data();
        }

        return result;
    }
    std::string getIPAddressForMAC(const std::string &macAddress, const std::string &nmapOutput)
    {
        // Create a regex pattern to match IP and MAC addresses
        std::regex macRegex(R"(Nmap scan report for (\d+\.\d+\.\d+\.\d+)[\s\S]*?MAC Address: ([0-9A-Fa-f:]+))");
        std::smatch match;

        std::string ipAddress;

        // Iterate over each match in the output
        auto searchStart = nmapOutput.cbegin();
        while (std::regex_search(searchStart, nmapOutput.cend(), match, macRegex))
        {
            std::string ip = match[1];  // Extract IP address
            std::string mac = match[2]; // Extract MAC address

            // If MAC address matches, return the corresponding IP address
            if (mac == macAddress)
            {
                ipAddress = ip;
                break;
            }

            searchStart = match.suffix().first; // Continue searching after the last match
        }

        return ipAddress;
    }
}

int main()
{
    try
    {
        // List of sites to test connectivity
        const std::vector<std::string> sites = {
            "8.8.8.8",
            "www.google.com",
            "www.amazon.com",
            "www.microsoft.com",
            "www.apple.com",
            "www.facebook.com",
            "www.youtube.com",
            "www.wikipedia.org"};

        // Timeout in seconds
        const int timeoutInSeconds = 5;

        // Check internet connectivity
        bool isConnected = InternetCheck::checkInternetConnectivity(sites, timeoutInSeconds);

        if (isConnected)
        {
            InternetCheck::logMessage("Internet is connected!");
        }
        else
        {
            InternetCheck::logMessage("No internet connectivity detected.");

            std::string command = "sudo nmap -sn 192.168.1.0/24";
            std::string targetMac = "E4:5F:01:31:B3:75";

            std::string output = InternetCheck::exec(command.c_str());
            std::string esp32IP = InternetCheck::getIPAddressForMAC(targetMac.c_str(), output.c_str());


            std::cout << esp32IP << std::endl;
        }

        return 0;
    }
    catch (const std::exception &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}
