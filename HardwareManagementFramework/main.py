import os
from dotenv import load_dotenv
from RouterManager.RouterManager import RouterManager

load_dotenv()


def main():
    """
    Entry point for the application.
    """
    try:
        myRouterManager = RouterManager()
    except Exception as e:
        print(f"Something Went Wrong: [{e}]")


if __name__ == "__main__":
    main()
