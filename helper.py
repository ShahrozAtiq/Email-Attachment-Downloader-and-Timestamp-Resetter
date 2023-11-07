
import json
import os
import filedate

def select_account(file_path):
    with open(file_path, 'r') as f:
        config_data = json.load(f)
    accounts = config_data.get('accounts', [])
    if not accounts:
        print("No accounts found in the config data.")
        return None
    
    print("Select a username by number:")
    for idx, account in enumerate(accounts, 1):
        print(f"{idx}. {account['username']}")

    while True:
        try:
            choice = int(input("Enter the number of the username you want to select: "))
            if 1 <= choice <= len(accounts):
                return accounts[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def uniquify_file_path(file_path):
    if not os.path.exists(file_path):
        return file_path

    # Split the file path into base directory, filename, and extension
    base_dir, file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(file_name)

    # Start with a counter of 1
    counter = 1

    while True:
        # Create a new filename with the counter
        new_file_name = f"{file_name} ({counter}){file_extension}"
        new_file_path = os.path.join(base_dir, new_file_name)

        # If the new file path doesn't exist, return it
        if not os.path.exists(new_file_path):
            return new_file_path

        # Increment the counter to try the next number
        counter += 1
def change_file_timestamp(file_path, timestamp):
    filedate.File(file_path).set(
        created = timestamp,
        modified = timestamp,
        accessed = timestamp
    )