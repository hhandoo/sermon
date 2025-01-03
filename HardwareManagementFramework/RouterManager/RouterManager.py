import time
import socket
from typing import List
from HardwareManagementFramework.SerialCommunication.SerialCommunication import (
    SerialCommunication,
)


class RouterManager(SerialCommunication):
    """
    A specialized class for communicating with a specific device.
    Inherits from SerialCommunication.
    """

    def __init__(self, port: str = None, baud_rate: int = 9600, timeout: int = 5):
        super().__init__(port, baud_rate, timeout)

    def restart_router(self) -> List[str]:
        """
        Sends a device-specific command and processes the response.

        Args:
            command (str): The command to send.

        Returns:
            List[str]: Processed response from the device.
        """
        # self.open_port()
        # try:
        #     response = self.send_command(command)
        #     # Perform additional processing if needed
        #     return response
        # finally:
        #     self.close_port()

    def check_connection(self, host: str, port: int = 53, timeout: int = 3) -> bool:
        """
        Checks if a specific host and port are reachable.

        Args:
            host (str): The host to connect to.
            port (int): The port to connect to. Default is 53 (DNS).
            timeout (int): Connection timeout in seconds. Default is 3 seconds.

        Returns:
            bool: True if the host is reachable, False otherwise.
        """
        try:
            socket.setdefaulttimeout(timeout)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
            return True
        except socket.error:
            return False

    def is_internet_available(self) -> bool:
        """
        Checks if the internet is available by testing multiple well-known DNS servers and websites.

        Returns:
            bool: True if any of the servers or websites are reachable, False otherwise.
        """
        # List of well-known DNS servers and websites
        test_targets = [
            ("8.8.8.8", 53),
            ("1.1.1.1", 53),
            ("9.9.9.9", 53),
            ("208.67.222.222", 53),
            ("www.google.com", 80),
            ("www.amazon.com", 80),
            ("www.facebook.com", 80),
            ("www.microsoft.com", 80),
            ("www.apple.com", 80),
        ]

        for host, port in test_targets:
            if self.check_connection(host, port):
                print(f"Successfully connected to {host}:{port}")
                return True

        print("Failed to connect to all test targets.")
        return False
