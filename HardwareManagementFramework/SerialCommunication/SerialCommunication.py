import os
import serial
import time
from typing import List


class SerialCommunication:
    """
    A class for handling serial communication with a device.
    """

    def __init__(self, port: str = None, baud_rate: int = 115200, timeout: int = 5):
        """
        Initializes the SerialCommunication instance.

        Args:
            port (str): The communication port (e.g., COM3 or /dev/ttyUSB0).
                        Defaults to the PORT environment variable if not provided.
            baud_rate (int): The baud rate for communication. Default is 9600.
            timeout (int): Timeout for reading from the port in seconds. Default is 5.
        """
        self.port = port or os.getenv("PORT")
        if not self.port:
            raise ValueError(
                "Communication port must be provided or set in the PORT environment variable."
            )

        self.baud_rate = baud_rate
        self.timeout = timeout
        self.__comm_port = None
        print(f"SerialCommunication initialized with port: {self.port}")

    def __enter__(self):
        """
        Enter the runtime context for the SerialCommunication instance.
        Opens the serial port.
        """
        self.__comm_port = serial.Serial(
            self.port, self.baud_rate, timeout=self.timeout
        )
        print("Serial port opened.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context for the SerialCommunication instance.
        Closes the serial port.
        """
        if self.__comm_port and self.__comm_port.is_open:
            self.__comm_port.close()
            print("Serial port closed.")

    def send_command(self, command_string: str) -> List[str]:
        """
        Sends a command string over the serial port and reads the response.

        Args:
            command_string (str): The command to send.

        Returns:
            List[str]: A list of response lines received from the device.
        """
        if not self.__comm_port or not self.__comm_port.is_open:
            raise ConnectionError("Serial port is not open.")

        try:
            print(f"Sending command: {command_string}")
            self.__comm_port.write(command_string.encode("utf-8"))

            result = []
            while True:
                line = self.__comm_port.readline().decode("utf-8").strip()
                if line:
                    result.append(line)
                    print(f"Received response: {line}")
                    break
                time.sleep(0.1)

            return result

        except serial.SerialException as e:
            print(f"Serial communication error: {e}")
            raise

        except Exception as e:
            print(f"Unexpected error: {e}")
            raise


# # Example usage:
# if __name__ == "__main__":
#     try:
#         with SerialCommunication() as comm:
#             response = comm.send_command("1 0 1 0 1 0 1 1\n")
#             print("Response from device:", response)
#     except Exception as e:
#         print(f"Error during communication: {e}")
