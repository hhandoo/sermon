import os
import argparse

from dotenv import load_dotenv
from RouterManager.RouterManager import RouterManager
from Command.Command import Command

load_dotenv()


def main():
    """
    Entry point for the application.
    """
    parser = argparse.ArgumentParser(
        description="CLI tool for monitoring and command execution"
    )

    parser.add_argument(
        "--auto", action="store_true", help="Enable Auto Monitor Mode"
    )  # Fix: Boolean flag
    parser.add_argument("--on-demand-command", type=str, help="Send Command")
    parser.add_argument(
        "--get-states", action="store_true", help="Get list of all states"
    )

    args = parser.parse_args()

    try:
        if args.auto:
            RouterManager()
        if args.on_demand_command:
            my_com = Command()
            my_com.send_command_to_MC(command=args.on_demand_command, desc="On Demand")
        if args.get_states:
            my_com = Command()
            resp = my_com.get_all_states()
            print(resp)
    except Exception as e:
        print(f"Something Went Wrong: [{e}]")


if __name__ == "__main__":
    main()
