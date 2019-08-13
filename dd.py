
import subprocess

print("[+] Starting Dumping [+]")
cap=subprocess.call(["airodump-ng","wlan0mon"])
