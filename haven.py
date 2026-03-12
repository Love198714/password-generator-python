import subprocess
import os
import time
import getpass

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92m" + "="*45)
    print("      RESTRICTED ACCESS: HILDA'S TECH HAVEN")
    print("="*45 + "\033[0m")
    
    password = getpass.getpass("Enter Security Key: ")
    
    if password == "hilda2026":
        print("\033[92mAccess Granted. Welcome, Hilda.\033[0m")
        time.sleep(1)
        return True
    else:
        print("\033[91mAccess Denied. Terminal Locked.\033[0m")
        time.sleep(2)
        return False

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[92m" + "="*45)
    print("      HILDA'S TECH HAVEN - SECURITY SUITE")
    print("="*45 + "\033[0m")
    print("[1] 🔑 Password Generator")
    print("[2] 📡 Port Scanner")
    print("[3] 🛡️  Hash Integrity Auditor")
    print("[4] 👃 DHCP Network Sniffer")
    print("[5] ❌ Exit")
    print("\033[92m" + "="*45 + "\033[0m")

def run_script(script_name):
    try:
        # subprocess.run launches the script as a new process
        subprocess.run(["python", script_name], check=True)
        input("\n\033[94mPress Enter to return to menu...\033[0m")
    except Exception as e:
        print(f"\033[91mError running {script_name}: {e}\033[0m")
        input("Press Enter to continue...")
def main():
    if login():
        while True:
            display_menu()
            choice = input("Selection > ")

            if choice == '1':
                # This forces 4 of each character type for a total of 16 'Elite' characters
                subprocess.run(["python", "password_generator.py", "-u", "4", "-l", "4", "-n", "4", "-s", "4"], check=True)
                input("\n\033[94mPress Enter to return to menu...\033[0m")
            elif choice == '2':
                run_script("port_scanner.py")
            elif choice == '3':
                run_script("hash_generator.py")
            elif choice == '4':
                run_script("dhcp_listener.py")
            elif choice == '5':
                print("Exiting Hilda's Tech Haven. Stay secure!")
                break
            else:
                print("Invalid selection. Try again.")
                time.sleep(1)

if __name__ == "__main__":
    main()