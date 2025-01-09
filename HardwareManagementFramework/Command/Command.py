import socket
from SerialCommunication.SerialCommunication import SerialCommunication


class Command:
    def __init__(self):
        pass

    def send_command_to_MC(self, command: str):
        if command != None and command != "":
            try:
                with SerialCommunication() as comm:
                    response = comm.send_command(f"{command}\n")
                    return "Response from device: " + response
            except Exception as e:
                print(f"Error during communication: {e}")
