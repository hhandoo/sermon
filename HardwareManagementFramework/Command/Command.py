import json
from datetime import datetime
from SerialCommunication.SerialCommunication import SerialCommunication
from DatabaseController.DatabaseController import DatabaseController
from NotificationSystem.NotificationSystem import NotificationSystem


class Command:
    def __init__(self):
        self._DatabaseController = DatabaseController()
        self._NotificationSystem = NotificationSystem()

    def send_command_to_MC(
        self, command: str, port: str = None, desc: str = "NA"
    ) -> str:
        if command != None and command != "":
            try:
                if port:
                    with SerialCommunication(port=port) as comm:
                        old_command = json.loads(self.get_last_command())
                        old_state = old_command["switch_states"]
                        old_desc = old_command["state_description"]
                        old_time = old_command["valid_from"]

                        response = comm.send_command(f"{command}\n")
                        updated_state = response[0]

                        self.save_command(updated_state, desc)

                        self.trigger_notification(
                            old_state,
                            old_desc,
                            old_time,
                            updated_state,
                            desc,
                            datetime.now(),
                        )

                        return response
                else:
                    with SerialCommunication() as comm:
                        old_command = json.loads(self.get_last_command())
                        old_state = old_command["switch_states"]
                        old_desc = old_command["state_description"]
                        old_time = old_command["valid_from"]

                        response = comm.send_command(f"{command}\n")
                        updated_state = response[0]

                        self.save_command(updated_state, desc)

                        self.trigger_notification(
                            old_state,
                            old_desc,
                            old_time,
                            updated_state,
                            desc,
                            datetime.now(),
                        )
                        return response
                    
                self._DatabaseController.close_connection()
            except Exception as e:
                print(f"Error during communication: {e}")

    def get_last_command(self) -> str:
        return self._DatabaseController.get_active_appliance_control()

    def save_command(self, current_state, current_desc) -> bool:
        print(current_desc, current_state)
        self._DatabaseController.update_and_insert_appliance_control(
            current_state, current_desc
        )

    def trigger_notification(
        self, old_state, old_desc, old_time, new_state, new_desc, new_time
    ):
        html_text = f"""
        <h1>Sermon Appliance Control v1.0</h1>
        <p>Dear Admin,</p>
        <p>The state of the appliance has been changed successfully:</p>
        <table border="1" cellspacing="0" cellpadding="8">
            <tr>
                <th>Attribute</th>
                <th>Previous</th>
                <th>New</th>
            </tr>
            <tr>
                <td>State</td>
                <td>{old_state}</td>
                <td>{new_state}</td>
            </tr>
            <tr>
                <td>Description</td>
                <td>{old_desc}</td>
                <td>{new_desc}</td>
            </tr>
            <tr>
                <td>Time</td>
                <td>{old_time}</td>
                <td>{new_time}</td>
            </tr>
        </table>
        <p>If this change was not expected, please review the system logs.</p>
        """

        self._NotificationSystem.send_mailjet_email(
            "handoo.harsh@gmail.com",
            "handoo.harsh@gmail.com",
            "State Change Notification",
            html_text,
        )
