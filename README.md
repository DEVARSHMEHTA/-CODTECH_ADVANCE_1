# CODTECH_ADVANCE_1
# Integrity Checker
## Details
- Name    : Devarsh Mehta
- Company : CODTECH IT SOLUTIONS PVT.LTD
- ID      : CT08DAL
- Domain  : Cyber Security & Ethical Hacking
- Duration: 20th Dec 2024 To 20th Jan 2025
- Mentor  : Neela Santhosh Kumar

## Overview
The **Integrity Checker** is a tool to monitor files for any changes and log their hash history with timestamps and dates. The tool calculates the hash of a file using various hash algorithms (SHA-1, SHA-256, MD5) and checks for any changes over time, providing a history of file integrity checks.

## Features

- Calculates the hash of a file using the specified algorithm (SHA-1, SHA-256, MD5).
- Monitors files for any changes and logs the hash history with timestamps and dates.
- Displays a history of file integrity checks.
- Supports Windows and Linux/Unix file paths.
- Uses Colorama and Termcolor for colorful terminal output.
- Creates a banner using PyFiglet.

## Requirements

- Python 3.x
- Packages: hashlib, termcolor, pyfiglet, os, datetime, json, colorama

You can install the required packages using pip:

```sh
pip install termcolor pyfiglet colorama
```
## Usage
1. Clone or download the repository.

2. Open a terminal and navigate to the project directory.

3. Provide Executable Permission.  

4. Run the integrity_checker.py script:

## Commands Paste It on terminal

```sh
git clone https://github.com/DEVARSHMEHTA/CODTECHADVANCE_T1.git
```

```sh
cd CODTECHADVANCE_T1
```

```sh
pip install -r requirements.txt
```

```sh
chmod +x integrity_checker.py
```

```sh
python3 integrity_checker.py
```
## Example Output

![image](https://github.com/user-attachments/assets/c09cf3d9-f593-43d1-a772-ca84b67b3e44)


## Author
- Devarsh Mehta
- [GitHub Profile](https://github.com/DEVARSHMEHTA)

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Acknowledgments

- [pyfiglet](https://github.com/pwaller/pyfiglet): ASCII art generation
- [termcolor](https://pypi.org/project/termcolor/): Colored terminal text
