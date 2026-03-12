import socket

def scan_port(ip, port):
    try:
        # Create a socket object (AF_INET = IPv4 address, SOCK_STREAM = TCP protocol)
        # This is like picking up a digital telephone
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a 0.5 second timeout. If the 'door' doesn't answer fast, move on.
        s.settimeout(0.5)
        
        # connect_ex returns 0 if the connection is successful (the port is open)
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"\033[92m[+] Port {port} is OPEN\033[0m")
        else:
            # Optional: print(f"[-] Port {port} is closed")
            pass
            
        s.close()
        
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# --- Test Section ---
# Now we ask the user which IP they want to audit
target_ip = input("Enter the IP address to scan (e.g., 127.0.0.1): ") 
print(f"Scanning target: {target_ip}...")

# List of common ports to check
# 21: FTP | 22: SSH | 80: HTTP | 443: HTTPS
# Ask the user for the range they want to scan
start_port = int(input("Enter start port (e.g., 1): "))
end_port = int(input("Enter end port (e.g., 100): "))

print(f"Scanning {target_ip} from port {start_port} to {end_port}...")

# We use +1 because range() stops one number before the end
for p in range(start_port, end_port + 1):
    scan_port(target_ip, p)

print("\033[92m\nScan complete.\033[0m")