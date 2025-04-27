# Port Scanner

This is a simple Python script that scans a range of ports on a target IP address to check for open ports. The script makes use of Python's `socket` library to attempt connections to the specified ports and reports which ones are open.

## Features
- Scans a range of ports on a target IP address.
- Reports open ports within the specified range.
- Handles errors and connection issues.

## Prerequisites
- Python 3.x (Recommended version: Python 3.6 or later)

## How to Use

### 1. Clone the Repository
To clone this repository, run the following command:
```bash
git clone https://github.com/yourusername/port-scanner.git
2. Run the Script
Navigate to the directory where you cloned the repository, then execute the script:

bash
Copy
Edit
cd port-scanner
python port_scanner.py
3. Input
The script will prompt you to enter:

The target IP address (e.g., 192.168.1.1).

The starting port (between 0 and 65535).

The ending port (between 0 and 65535).

Example
bash
Copy
Edit
Enter the IP address to scan: 192.168.1.1
Enter the starting port (0-65535): 80
Enter the ending port (0-65535): 100
Scanning 192.168.1.1 from port 80 to 100...
Port 80 is OPEN
Port 443 is OPEN

Open Ports: [80, 443]
Error Handling
Invalid IP address format.

Invalid port range.

Connection errors.

License
This project is licensed under the MIT License - see the LICENSE file for details.

bash
Copy
Edit

### Notes:
- Be sure to replace `https://github.com/yourusername/port-scanner.git` with the actual URL of your GitHub repository.
- You can update the "LICENSE" link to reflect the license you choose for the repository
