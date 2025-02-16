import os
from dotenv import load_dotenv
from RouterManager.RouterManager import RouterManager
from DatabaseController.DatabaseController import DatabaseController

load_dotenv()


def main():
    """
    Entry point for the application.
    """
    try:
        # RouterManager()

        db = DatabaseController()

        active_record = db.get_active_appliance_control()
        print("Active Record:", active_record)

        # Insert a new record (this will also update the previous active record)
        db.update_and_insert_appliance_control("1110", "Fan ON")

        # Close connection
        db.close_connection()
    except Exception as e:
        print(f"Something Went Wrong: [{e}]")


if __name__ == "__main__":
    main()
