"""
A to-do list tracker

Based on the the examples given at
https://pyflo.net/todo/
"""

import os


FILE_NAME = "todolist.txt"


def main():
    """
    Let's begin
    """
    command = ""
    try:
        while command != "exit":
            show_list()
            command = input("Add, remove, or exit? ").lower().strip()
            if command == "add":
                task = input("What task would you like to add? ")
                add_to_list(task)
            elif command == "remove":
                number = int(input("Which task would you like to remove? "))
                remove_from_list(number)

        print("Goodbye!")
    except (EOFError, KeyboardInterrupt, ValueError):
        pass


def show_list():
    """
    Show the todo-list.
    """
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("\nThe list is empty.\n")
                return
            print()
            for index, line in enumerate(lines):
                print(f"({index+1}) {line}", end='')
            print()
    except FileNotFoundError:
        print("\nThere is no list yet.\n")


def add_to_list(task):
    """
    Add a task to the list.
    """
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(task)
            file.write(os.linesep)
    except FileNotFoundError:
        print("Unable to add the task to the list. File not found.")


def remove_from_list(number):
    """
    Remove an item from the list.
    """
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file1:
            lines = file1.readlines()

        if number < 1 or number > len(lines):
            print("\nNo such item")
            return

        with open(FILE_NAME, "w", encoding="utf-8") as file2:
            for index, line in enumerate(lines):
                if index+1 != number:
                    file2.write(line)

    except FileNotFoundError:
        print("Unable to remove the task. The file has gone missing.")


if __name__ == "__main__":
    main()
