🔎 Simple Python Port Scanner
Description
This is a lightweight Port Scanner built in Python.
It allows you to scan a range of ports on a given IP address to detect open ports.
The tool uses the socket library to attempt TCP connections to each port within the specified range.

Features
Scan any IP address for open TCP ports.

Define custom start and end port ranges (0–65535).

Quick timeout for faster scanning.

Validates the IP address format before scanning.

How to Use
Clone or download the repository.

Make sure you have Python 3 installed.

Run the script:

bash
Copy
Edit
python port_scanner.py
Enter the target IP address when prompted.

Enter the starting and ending ports you want to scan.

Example:

bash
Copy
Edit
Enter the IP address to scan: 192.168.1.1
Enter the starting port (0-65535): 20
Enter the ending port (0-65535): 80
Example Output
bash
Copy
Edit
Scanning 192.168.1.1 from port 20 to 80...
Port 22 is OPEN
Port 80 is OPEN

Open Ports: [22, 80]
Requirements
Python 3.x

(Uses only built-in Python libraries — no additional packages required.)

Notes
The script uses a timeout of 0.5 seconds for each port to ensure quick scanning.

Designed for educational and authorized use only. Do not scan IPs without permission!

License
This project is open-source and available under the MIT License.

Author
B0lB0l
