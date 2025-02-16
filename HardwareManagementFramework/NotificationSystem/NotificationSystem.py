import os
import json
from mailjet_rest import Client


class NotificationSystem:

    def __init__(self):
        self._API_KEY = os.getenv("API_KEY")
        self._SECRET_KEY = os.getenv("SECRET_KEY")
        self.initialize_mailjet_client()

    def initialize_mailjet_client(self):
        self._mailjet = Client(auth=(self._API_KEY, self._SECRET_KEY), version="v3.1")

    def send_mailjet_email(self, sender_email, receiver_email, subject, htmlText):
        """Send an email using Mailjet API."""
        data = {
            "Messages": [
                {
                    "From": {"Email": sender_email, "Name": "Sermon Appliance Control"},
                    "To": [{"Email": receiver_email, "Name": "Admin"}],
                    "Subject": subject,
                    "HTMLPart": htmlText,
                }
            ]
        }

        # Send request to Mailjet
        response = self._mailjet.send.create(data=data)
        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Error sending email: {response.status_code} - {response.text}")
