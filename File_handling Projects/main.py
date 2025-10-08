# File Handling Projects - CRUD Operations

from pathlib import Path  # Importing Path from pathlib module
base_path = Path('.')  # Use current directory as base


def read_fileandfolder():
    """List all files and folders in the current directory."""
    items = list(base_path.rglob('*'))  # for all files and folders
    print("\n Available Files & Folders:")
    if items:
        for i, item in enumerate(items):  # for indexing
            print(f"{i + 1}. {item}")
    else:
        print("No files or folders found.")


def create_file():
    try:
        read_fileandfolder()
        name = input("\nEnter the file name with extension: ")
        p = Path(name)

        if not p.exists():
            with open(p, 'w') as fs:
                data = input("Enter the data to be written in the file: ")
                fs.write(data)
            print(f"\n File '{name}' created successfully.")
        else:
            print(f"\n File '{name}' already exists.")

    except Exception as e:
        print(f"\n An error occurred: {e}")


def read_file():
    try:
        read_fileandfolder()
        name = input("\nEnter the file name with extension to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(f"\n Contents of '{name}':\n{data}")
        else:
            print(f"\n File '{name}' does not exist.")
    except Exception as e:
        print(f"\n An error occurred: {e}")


def update_file():
    try:
        read_fileandfolder()
        name = input("\nEnter the file name with extension to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("\nChoose what to do:")
            print("1. Change the file name")
            print("2. Overwrite the content")
            print("3. Append new content")

            res = int(input("\nEnter your choice: "))

            if res == 1:
                new_name = input("Enter the new file name with extension: ")
                new_path = Path(new_name)
                p.rename(new_path)
                print(f"\n File renamed to '{new_name}' successfully.")

            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter the new data to overwrite the file: ")
                    fs.write(data)
                print(f"\n File '{name}' overwritten successfully.")

            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Enter the data to append to the file: ")
                    fs.write("\n" + data)
                print(f"\n Data appended to '{name}' successfully.")

            else:
                print("\n Invalid choice.")
        else:
            print(f"\n File '{name}' does not exist.")
    except Exception as e:
        print(f"\n An error occurred: {e}")


def delete_file():
    try:
        read_fileandfolder()
        name = input("\nEnter the file name with extension to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print(f"\n File '{name}' deleted successfully.")
        else:
            print(f"\n File '{name}' does not exist.")
    except Exception as e:
        print(f"\n An error occurred: {e}")


# -------- Main Menu --------
print("\n===== FILE HANDLING - CRUD OPERATIONS =====")
print("Press 1 to Create a file")
print("Press 2 to Read a file")
print("Press 3 to Update a file")
print("Press 4 to Delete a file")

try:
    check = int(input("\nPlease enter your choice: "))

    if check == 1:
        create_file()
    elif check == 2:
        read_file()
    elif check == 3:
        update_file()
    elif check == 4:
        delete_file()
    else:
        print("\n Invalid choice! Please choose between 1–4.")
except ValueError:
    print("\n Invalid input. Please enter a number.")
