from Command.Command import Command

myCommand = Command()

resp = myCommand.send_command_to_MC(command="1111", port="/dev/ttyUSB0")

print(resp)
