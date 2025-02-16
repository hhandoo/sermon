from mailjet_rest import Client
import json

# Mailjet API credentials


# Initialize Mailjet Client
mailjet = Client(auth=(API_KEY, SECRET_KEY), version="v3.1")


def send_mailjet_email(sender_email, receiver_email, subject, htmlText):
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
    response = mailjet.send.create(data=data)
    if response.status_code == 200:
        print("Email sent successfully!")
    else:
        print(f"Error sending email: {response.status_code} - {response.text}")


# Example Usage
send_mailjet_email(
    "handoo.harsh@gmail.com",
    "handoo.harsh@gmail.com",
    "State Change Notification",
    """
    <h1>Sermon Appliance Control v1.0</h1>
    <p>Dear Admin,</p>
    <p>The state of the appliance has been changed successfully:</p>
    <p>Previous State: 0000 </p>
    <p>New State: 0011</p>
    <p>If this change was not expected, please review the system logs.</p>
    """,
)
