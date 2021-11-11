import os
import threading
from enum import IntEnum
from time import sleep
from threading import Thread
from puml_builder import build_uml, visualize_uml

# Constant
SLEEP_TERM = 1

# Global variable
USER_INPUT = ""
APP_DATA = ""
PARSED_APP_DATA = dict()
PARSED_APP_DATA_LOCK = threading.Lock()


class C(IntEnum):
    COMPONENT = 1
    TYPE = 2
    TRAITS = 3
    PHASE = 4
    HEALTHY = 5
    STATUS = 6
    CREATED_TIME = 7


def print_usage():
    print()
    print("--------------------- Usage --------------------")
    print("> p          - Show entire application")
    print("> l          - Show application list with app_name")
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

    # Initialize global variables
    APP_DATA = app_data
    PARSED_APP_DATA.clear()

    app_data = APP_DATA.split("\n")
    app_name = ""

    for i in range(1, len(app_data) - 1):
        # Separate words
        item = app_data[i].split("\t")
        for j in range(len(item)):
            item[j] = item[j].strip()

        # Get an application name
        if item[0] != "├─" and item[0] != "└─":
            app_name = item[0]

        if app_name not in PARSED_APP_DATA:
            PARSED_APP_DATA[app_name] = []

        temp = dict()
        temp["component"] = item[C.COMPONENT]
        temp["type"] = item[C.TYPE]
        temp["traits"] = item[C.TRAITS]
        temp["phase"] = item[C.PHASE]
        temp["healthy"] = item[C.HEALTHY]
        temp["status"] = item[C.STATUS]
        temp["created_time"] = item[C.CREATED_TIME]

        PARSED_APP_DATA[app_name].append(temp)

    print("\nChanges in the application have been detected")
    print(APP_DATA)

    PARSED_APP_DATA_LOCK.release()


def print_app():
    global APP_DATA, PARSED_APP_DATA_LOCK

    # Get latest app data
    update_app_data()

    if APP_DATA == "":
        print("There is no application running")
        return

    PARSED_APP_DATA_LOCK.acquire()
    print(APP_DATA)
    PARSED_APP_DATA_LOCK.release()


def print_app_list():
    global PARSED_APP_DATA, PARSED_APP_DATA_LOCK

    # Get latest app data
    update_app_data()

    PARSED_APP_DATA_LOCK.acquire()

    # Case: No application
    if len(PARSED_APP_DATA) == 0:
        print("There is no application running\n")
        PARSED_APP_DATA_LOCK.release()
        return

    # Print the application list
    print("APP LIST")
    for key in PARSED_APP_DATA:
        print(key)
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
        print('Application "', app_name, '" is not exist\n', sep="")
        PARSED_APP_DATA_LOCK.release()
        return

    build_uml(app_name, PARSED_APP_DATA[app_name])
    visualize_uml()

    PARSED_APP_DATA_LOCK.release()


# Update the application information every SLEEP_TERM
def thread1_routine():
    global APP_DATA

    while True:
        update_app_data()
        sleep(SLEEP_TERM)


# Handle user input
def thread2_routine():
    global USER_INPUT, PARSED_APP_DATA, PARSED_APP_DATA_LOCK

    sleep(1)
    print_usage()

    while True:
        print("> ", end="")
        USER_INPUT = input()
        print()

        if USER_INPUT == "":
            continue

        elif USER_INPUT == "q":
            print("Terminate the program")
            break

        elif USER_INPUT == "p":
            print_app()

        elif USER_INPUT == "l":
            print_app_list()

        elif USER_INPUT[0] == "v":
            visualize_app_data()

        else:
            print("Error, unknown command\n")


if __name__ == "__main__":
    thread1 = Thread(target=thread1_routine)
    thread2 = Thread(target=thread2_routine)

    thread1.daemon = True
    thread2.daemon = True

    thread1.start()
    thread2.start()

    thread2.join()
