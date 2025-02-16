import socket
from SerialCommunication.SerialCommunication import SerialCommunication


class Command:
    def __init__(self):
        pass

    def send_command_to_MC(self, command: str, port: str = None) -> str:
        if command != None and command != "":
            try:
                if port:
                    with SerialCommunication(port=port) as comm:
                        response = comm.send_command(f"{command}\n")
                        return response
                else:
                    with SerialCommunication() as comm:
                        response = comm.send_command(f"{command}\n")
                        return response
            except Exception as e:
                print(f"Error during communication: {e}")

    def get_last_command(self) -> str:
        pass

    def save_command(self) -> bool:
        pass
