
import subprocess

print("[+] Start Dumping [+]")
cap=subprocess.call(["airodump-ng","wlan0mon"])
