import socket

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            return result == 0
    except Exception:
        return False

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    host = "127.0.0.1"
    print(f"Scanning {host}")
    open_ports = scan_ports(host, 20, 1024)

    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports detected.")