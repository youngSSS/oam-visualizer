import os
import threading
from enum import Enum
from time import sleep
from threading import Thread

# Constant
SLEEP_TERM = 5

# Global variable
USER_INPUT = ""
APP_DATA = ""
PARSED_APP_DATA = dict()
PARSED_APP_DATA_LOCK = threading.Lock()


class C(Enum):
    COMPONENT = 0
    TYPE = 1
    TRAITS = 2
    PHASE = 3
    HEALTHY = 4
    STATUS = 5
    CREATED_TIME = 6
    CHILD = 7


def print_usage():
    print()
    print("--------------------- Usage --------------------")
    print("> s          - Show application list with app_id")
    print("> v app_name - Visualize application status")
    print("> q          - Terminate the program")
    print("------------------------------------------------")
    print()


def update_app_data():
    global APP_DATA, PARSED_APP_DATA, PARSED_APP_DATA_LOCK

    app_data = os.popen("vela ls").read()

    # Case: No changes
    if APP_DATA == app_data:
        return

    # Case: Changes
    PARSED_APP_DATA_LOCK.acquire()

    APP_DATA = app_data
    app_data = APP_DATA.split("\n")
    parent_component = ""
    for i in range(1, len(app_data) - 1):
        # Separate words
        item = app_data[i].split("\t")
        for j in range(len(item)):
            item[j] = item[j].strip()

        # Case: Child component
        if item[0] == "├─" or item[0] == "└─":
            PARSED_APP_DATA[parent_component].append(item[1:])
        # Case: Parent component
        else:
            PARSED_APP_DATA[item[0]] = item[1:]
            parent_component = item[0]

    print(APP_DATA)

    PARSED_APP_DATA_LOCK.release()


def print_app_list():
    global PARSED_APP_DATA, PARSED_APP_DATA_LOCK

    # Get latest app data
    update_app_data()

    PARSED_APP_DATA_LOCK.acquire()

    # Case: No application
    if len(PARSED_APP_DATA) == 0:
        print("\nThere is no application running\n")
        PARSED_APP_DATA_LOCK.release()
        return

    # Print the application list
    print("\nAPP LIST")
    for key in PARSED_APP_DATA:
        print("> " + key)
    print()

    PARSED_APP_DATA_LOCK.release()


def visualize_app_data():
    global USER_INPUT, PARSED_APP_DATA, PARSED_APP_DATA_LOCK

    app_name = USER_INPUT[2:]

    if app_name == "" or USER_INPUT[1] != " ":
        print("Command format error, please follow below usage")
        print_usage()
        return

    # Get latest app data
    update_app_data()

    PARSED_APP_DATA_LOCK.acquire()

    if app_name not in PARSED_APP_DATA:
        print("\nApplication", app_name, "is not exist\n")
        PARSED_APP_DATA_LOCK.release()
        return

    print(PARSED_APP_DATA)

    PARSED_APP_DATA_LOCK.release()


# Handle user input
def thread2_routine():
    global USER_INPUT, PARSED_APP_DATA, PARSED_APP_DATA_LOCK

    while True:
        USER_INPUT = input()

        if USER_INPUT == "q":
            print("Terminate the program")
            break

        elif USER_INPUT == "s":
            print_app_list()

        elif USER_INPUT[0] == "v":
            visualize_app_data()

        else:
            print("Error, unknown command")


# Update the application information every SLEEP_TERM
def thread1_routine():
    global APP_DATA

    while True:
        update_app_data()
        sleep(SLEEP_TERM)


if __name__ == "__main__":
    print_usage()

    thread1 = Thread(target=thread1_routine)
    thread2 = Thread(target=thread2_routine)

    thread1.daemon = True
    thread2.daemon = True

    thread1.start()
    thread2.start()

    thread2.join()
