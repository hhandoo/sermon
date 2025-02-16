from Command.Command import Command
from dotenv import load_dotenv
load_dotenv()
myCommand = Command()
resp = myCommand.send_command_to_MC(command="1111", port="/dev/ttyUSB0", desc="All On")
print(resp)
