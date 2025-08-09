import os

# Ask user for directory path
path = input("Enter the directory path: ")

try:
    # List all entries in the directory
    entries = os.listdir(path)
    
    print(f"\nContents of '{path}':\n")
    for entry in entries:
        full_path = os.path.join(path, entry)  # Get the absolute path
        if os.path.isfile(full_path):
            print(f"[FILE]      {entry}")
        elif os.path.isdir(full_path):
            print(f"[DIRECTORY] {entry}")
        else:
            print(f"[OTHER]     {entry}")

except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied for accessing '{path}'.")
