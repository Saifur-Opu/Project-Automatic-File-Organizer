import socket

# Target IP (your own PC for testing)
target = input("Enter IP address (e.g. 127.0.0.1): ")

# Port range to scan
start_port = 443
end_port = 444

print(f"\nScanning {target}...\n")

for port in range(start_port, end_port + 1):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

    s.close()

print("\nScan complete.")