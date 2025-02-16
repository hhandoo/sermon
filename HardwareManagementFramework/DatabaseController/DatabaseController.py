import os
import json
import pyodbc


class DatabaseController:

    def __init__(self):
        self._host = os.getenv("DB_HOST")
        self._database = os.getenv("DB_NAME")
        self._user = os.getenv("DB_USER")
        self._password = os.getenv("DB_PASSWORD")
        self._port = os.getenv("DB_PORT")

        self.__connection = None

    def _connect(self):
        """Protected method to establish a database connection."""
        try:
            self.__connection = pyodbc.connect(
                f"DRIVER={{PostgreSQL Unicode}};"
                f"SERVER={self._host};"
                f"PORT={self._port};"
                f"DATABASE={self._database};"
                f"UID={self._user};"
                f"PWD={self._password};"
            )
        except Exception as e:
            print(f"Connection error: {e}")

    def get_conn(self):
        return self.__connection

    def _disconnect(self):
        """Protected method to close the database connection."""
        if self.__connection:
            self.__connection.close()
            print("Database connection closed.")

    def _execute_query(self, query, fetch=False):
        """Protected method to execute a SQL query."""
        if not self.__connection:
            self._connect()

        try:
            cursor = self.__connection.cursor()
            cursor.execute(query)

            if fetch:
                results = cursor.fetchall()
                cursor.close()
                return results

            self.__connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Query execution error: {e}")
            return None

    def get_active_appliance_control(self) -> str:
        """Public method to fetch active appliance control record as JSON."""
        query = "SELECT switch_states, state_description, valid_from FROM iot.get_active_appliance_control();"
        results = self._execute_query(query, fetch=True)
        if not results:
            return json.dumps([])
        try:
            cursor = self.__connection.cursor()
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            cursor.close()
            data = [dict(zip(columns, row)) for row in results]
            return json.dumps(data[0], default=str)

        except Exception as e:
            print(f"Error processing query results: {e}")
            return json.dumps([])

    def update_and_insert_appliance_control(self, switch_states, state_description):
        """Public method to update old record and insert a new one."""
        query = f"CALL iot.update_and_insert_appliance_control('{switch_states}', '{state_description}');"
        self._execute_query(query)

    def close_connection(self):
        """Public method to close the database connection."""
        self._disconnect()
