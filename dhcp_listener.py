from scapy.all import sniff, Ether, DHCP
import time

def print_packet(packet):
    # Initialize variables
    target_mac, requested_ip, hostname, vendor_id = [None] * 4

    # 1. Capture the MAC address from the Ethernet layer
    if packet.haslayer(Ether):
        target_mac = packet.getlayer(Ether).src

    # 2. Extract details from the DHCP options
    if packet.haslayer(DHCP):
        for item in packet[DHCP].options:
            try:
                label, value = item
            except ValueError:
                continue

            if label == 'requested_addr':
                requested_ip = value
            elif label == 'hostname':
                hostname = value.decode()
            elif label == 'vendor_class_id':
                vendor_id = value.decode()

    # 3. If we caught a device requesting an IP, display it
    
    if target_mac and requested_ip:
        time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
        print(f"\033[92m{time_now} : {target_mac} - {hostname} / {vendor_id} requested {requested_ip}\033[0m")
        
        with open("network_audit_log.txt", "a") as log_file:
            log_file.write(f"{time_now} : {target_mac} - {hostname} / {vendor_id} requested {requested_ip}\n")

def listen_dhcp():
    print("--- Hilda's Tech Haven: DHCP Listener Active ---")
    print("Monitoring network for new device connections...")
    
    # prn=print_packet tells Scapy to run our function for every packet found
    # filter='udp and (port 67 or port 68)' keeps the noise out
    sniff(prn=print_packet, filter='udp and (port 67 or port 68)', store=0)

if __name__ == "__main__":
    listen_dhcp()