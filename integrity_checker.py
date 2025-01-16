import hashlib
from termcolor import colored
import pyfiglet
import os
from datetime import datetime
import json
from colorama import Fore, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Generate banner using pyfiglet
banner = pyfiglet.figlet_format("Integrity Checker")
creator_details = "--- by Devarsh Mehta"

# Print banner and creator details
print(colored(banner, 'cyan'))
print(colored(creator_details, 'cyan'))

def compute_file_hash(filepath, hash_algo='sha256'):
    """
    Compute the hash of a file using the specified algorithm.
    :param filepath: Path to the file
    :param hash_algo: Hashing algorithm (sha1, sha256, md5)
    :return: Hexadecimal hash value
    """
    hash_obj = hashlib.new(hash_algo)
    with open(filepath, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def watch_file(filepath, hash_algo='sha256', log_file='history.json'):
    """
    Watch a file for any modifications and log its hash history.
    :param filepath: Path to the file
    :param hash_algo: Hashing algorithm (sha1, sha256, md5)
    :param log_file: Path to the JSON log file
    :return: None
    """
    if not os.path.exists(filepath):
        print(colored(f"Error: The file {filepath} does not exist.", 'red'))
        return

    current_hash = compute_file_hash(filepath, hash_algo)
    time_checked = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        'timestamp': time_checked,
        'filepath': filepath,
        'algorithm': hash_algo,
        'hash': current_hash
    }

    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            log_data = json.load(f)
    else:
        log_data = []

    if log_data and any(entry['hash'] == current_hash for entry in log_data):
        print(f"{Fore.GREEN}No changes detected for {filepath} using {hash_algo}.")
    else:
        print(f"{Fore.YELLOW}Hash for {filepath} ({hash_algo}): {Fore.CYAN}{current_hash}")
        if log_data:
            print(f"{Fore.RED}ALERT: Modifications detected in {filepath}.")
        else:
            print(f"{Fore.BLUE}Initiating monitoring for new file: {filepath}")
        log_data.append(log_entry)

        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=4)

        print(f"{Fore.YELLOW}Log updated. Timestamp: {time_checked}")

def show_log(log_file='history.json'):
    """
    Display the log of file integrity checks.
    :param log_file: Path to the JSON log file
    :return: None
    """
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            log_data = json.load(f)
            for entry in log_data:
                timestamp = entry.get('timestamp', 'N/A')
                filepath = entry.get('filepath', 'N/A')
                algorithm = entry.get('algorithm', 'N/A')
                file_hash = entry.get('hash', 'N/A')
                print(f"{Fore.YELLOW}Timestamp: {timestamp}")
                print(f"{Fore.BLUE}File: {filepath}")
                print(f"{Fore.CYAN}Algorithm: {algorithm}")
                print(f"{Fore.GREEN}Hash: {file_hash}\n")
    else:
        print(f"{Fore.RED}No log history found.")

# Determine the OS and set the prompt accordingly
if os.name == 'nt':  # For Windows
    prompt_msg = "Enter the file path (e.g., D:\\folder\\file.txt): "
else:  # For Linux/Unix
    prompt_msg = "Enter the file path (e.g., /home/user/folder/file.txt): "

# Get file path input from the user
file_path_input = input(colored(f"Enter the path of the file to monitor ({prompt_msg}): ", 'green'))

# Display the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(colored(f"Current time: {current_datetime}", 'magenta'))

# Watch the specified file
watch_file(file_path_input)

# Show the log of integrity checks
print(colored("\nFile Integrity Check Log:", 'magenta'))
show_log()
