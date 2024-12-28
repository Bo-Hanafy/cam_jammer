import os
from scapy.all import ARP, Ether, srp
import pyfiglet
from termcolor import colored

def print_banner():
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
    banner = pyfiglet.figlet_format("Network Scanner")
    print(colored(banner, "cyan"))
    print(colored("Created by Bo_Hanafy  🦅", "yellow"))
    print("-" * 50)

def scan_network(ip_range):
    arp_request = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    print_banner()
    network_range = input(colored("Enter the IP range (e.g., 192.168.1.0/24): ", "green"))
    print("\nScanning the network... 🔍\n")
    devices = scan_network(network_range)
    print(colored("Connected devices:", "blue"))
    print("-" * 50)
    for idx, device in enumerate(devices, start=1):
        print(f"{idx}. IP: {device['ip']} - MAC: {device['mac']}")
    print("-" * 50)
    print(colored(f"Total {len(devices)} device(s) found. ✅", "green"))

