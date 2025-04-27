import socket

def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...")
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5) 
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)
            sock.close()
        except socket.error as e:
            print(f"Couldn't connect to server: {e}")
            break

    if not open_ports:
        print("No open ports found in the specified range.")
    else:
        print(f"\nOpen Ports: {open_ports}")

def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    if not is_valid_ip(target_ip):
        print("Invalid IP address format!")
        exit()

    try:
        start_port = int(input("Enter the starting port (0-65535): "))
        end_port = int(input("Enter the ending port (0-65535): "))
        
        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
            print("Port numbers must be between 0 and 65535!")
            exit()

        if start_port > end_port:
            print("Starting port must be less than or equal to ending port!")
            exit()

        scan_ports(target_ip, start_port, end_port)

    except ValueError:
        print("Please enter valid numeric port numbers!")
