import time
import socket
import speedtest
import subprocess
from typing import List
from Command.Command import Command
from NotificationSystem.NotificationSystem import NotificationSystem


class RouterManager:
    """
    A specialized class for communicating with a specific device.
    Inherits from SerialCommunication.
    """

    def __init__(self):
        is_internet_available = self.is_internet_available()
        self._not = NotificationSystem()
        self.myCommand = Command()

        if is_internet_available == False:
            self.restart_router()
        else:
            print("Skipping Router Restart")

    def restart_router(self) -> List[str]:
        """
        Sends a device-specific command and processes the response.

        Args:
            command (str): The command to send.

        Returns:
            List[str]: Processed response from the device.
        """
        try:
            command = "bash -c 'source /home/sv_admin/production/sermon/triggers/on_demand_router_restart.sh'"
            subprocess.run(command, shell=True, check=True)
        except Exception as e:
            print(f"Error during communication: {e}")

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
        test_targets = [
            ("8.8.8.8", 53),
            # ("1.1.1.1", 53),
            # ("9.9.9.9", 53),
            # ("208.67.222.222", 53),
            # ("www.google.com", 80),
            # ("www.amazon.com", 80),
            # ("www.facebook.com", 80),
            # ("www.microsoft.com", 80),
            # ("www.apple.com", 80),
        ]

        for host, port in test_targets:
            if self.check_connection(host, port):
                print(f"Successfully connected to {host}:{port}")
                return True

        print("Failed to connect to all test targets.")
        return False

    def test_speed(self):
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping
        return download_speed, upload_speed, ping
