#include <iostream>
#include <boost/asio.hpp>
#include <boost/system/error_code.hpp>
#include <chrono>
#include <thread>

using namespace boost::asio;

int main()
{
    try
    {
        // Set up serial communication with Arduino
        io_service io;
        serial_port serial(io, "/dev/ttyACM0");               // Replace with your correct port
        serial.set_option(serial_port_base::baud_rate(9600)); // Set baud rate

        std::cout << "Successfully opened serial port!" << std::endl;

        // Command string (state of relays as space-separated values)
        std::string command = "1 0 1 0 1 0 1 0"; // Adjust this based on your needs

        // Send the command to the Arduino
        write(serial, buffer(command + "\n"));
        std::cout << "Sent command: " << command << std::endl;

        // Give Arduino some time to process and respond
        std::this_thread::sleep_for(std::chrono::milliseconds(500)); // Wait for Arduino to process

        // Read the response from the Arduino until a newline
        std::string response;
        char c;
        while (read(serial, buffer(&c, 1)) && c != '\n')
        {
            response += c; // Append each character to the response string
        }

        // Check if we received anything
        if (!response.empty())
        {
            std::cout << "Arduino response: " << response << std::endl;
        }
        else
        {
            std::cerr << "No response received from Arduino!" << std::endl;
        }
    }
    catch (const boost::system::system_error &e)
    {
        std::cerr << "Error: " << e.what() << std::endl;
        std::cerr << "Error Code: " << e.code() << std::endl;
    }

    return 0;
}
