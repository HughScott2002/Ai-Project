# CRUD Operations for module_master
from controller.db_connect import *


def insert_module(module: str, number_of_credits: int):
    try:
        query = f"INSERT INTO module_master (module, number_of_credits) VALUES (%s, %s)"
        values = (module, number_of_credits)
        cursor.execute(query, values)
        conn.commit()

        print("Module successfully inserted.")
        return "Success"
    except Exception as e:
        print(f"Error inserting Module: {e}")
        return "err"


# Retrieve all Modules
def retrieve_all_modules():
    try:
        cursor.execute("SELECT * FROM module_master")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving all modules: {e}")
        return "err"


# Retrieve a specific module by ID
def retrieve_module_master_by_id(module_id: str):
    try:
        cursor.execute(f"SELECT * FROM module_master WHERE module = '{module_id}'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Exception as e:
        print(f"Error retrieving module: ID#{module_id}")
        print(f"Error: {e}")
        return "err"


# Update a module
def update_module(module: str, credits: int):
    try:
        update_query = f"UPDATE module_master SET module = %s, number_of_credits = %s WHERE module_id = %s"
        update_values = (module, credits)
        cursor.execute(update_query, update_values)
        conn.commit()
        print("Module Update Successful")
        return "Success"
    except Exception as e:
        print(f"Error updating module: {e}")
        return "err"


# Delete a module
def delete_module(module_id):
    try:
        query = f"DELETE FROM module_master WHERE module_id = %s"
        values = (module_id,)
        cursor.execute(query, values)
        conn.commit()

        print("Module successfully deleted.")
        return "Success"

    except Exception as e:
        print(f"Error deleting module: {e}")
        return "err"


def delete_all_modules():
    try:
        query = "DELETE FROM module_master"
        cursor.execute(query)
        conn.commit()

        print("All Module successfully deleted.")
        return "Success"

    except Exception as e:
        print(f"Error deleting module: {e}")
        return "err"
