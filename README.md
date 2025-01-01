# Internet Connectivity and MAC to IP Lookup

This C++ program checks internet connectivity by pinging a list of sites and performs a MAC to IP address lookup using Nmap. If internet connectivity is unavailable, it will scan a local network for devices and return the IP address of a device with a specific MAC address.

## Features

- **Internet Connectivity Check**: Pings a list of predefined websites to verify internet connectivity.
- **Local Network Scan**: Uses Nmap to scan a local network and retrieve the IP address associated with a specific MAC address.
- **MAC to IP Mapping**: Searches Nmap's output for a specific MAC address and returns the corresponding IP address.

## Prerequisites

- Nmap must be installed on the system for local network scanning (`sudo nmap -sn 192.168.1.0/24`).
- The program uses the `timeout` and `ping` commands to check internet connectivity.
- C++11 or later compiler required.

## Compilation

To compile the code, run the following command:

```bash
sudo g++ -std=c++11 netmon.cpp -o netmon && ./netmon
```
