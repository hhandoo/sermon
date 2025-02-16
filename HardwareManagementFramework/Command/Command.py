from SerialCommunication.SerialCommunication import SerialCommunication
from DatabaseController.DatabaseController import DatabaseController
from NotificationSystem.NotificationSystem import NotificationSystem


class Command:
    def __init__(self):
        self._DatabaseController = DatabaseController()
        self._NotificationSystem = NotificationSystem()

    def send_command_to_MC(self, command: str, port: str = None) -> str:
        if command != None and command != "":
            try:
                if port:
                    with SerialCommunication(port=port) as comm:
                        response = comm.send_command(f"{command}\n")
                        updated_state = response[0][0]
                        print(response)
                        return response
                else:
                    with SerialCommunication() as comm:
                        response = comm.send_command(f"{command}\n")
                        updated_state = response[0][0]
                        print(response)
                        return response
            except Exception as e:
                print(f"Error during communication: {e}")

    def get_last_command(self) -> str:
        return self._DatabaseController.get_active_appliance_control()

    def save_command(self) -> bool:
        pass
