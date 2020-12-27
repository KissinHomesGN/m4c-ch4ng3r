#!/usr/bin/python3
#im getting back into programming and this was my first script i wrote back, im starting off basic and going through a few courses to get my grounding again but trying not to skid the code from the courses! Enjoy and use if you want
#version 1.2
import subprocess #runs system commands

#takes user input
mac = input("What would you like your MAC address to be?:")
intf = input("What interface would you like to change?:")
print("Working...")
#does system commands that are stated
subprocess.call("sudo ifconfig " + intf + " down, shell=True)
subprocess.call("sudo ifconfig " + intf + " hw ether " + mac + , shell=True)
subprocess.call("sudo ifconfig " + intf + " up", shell=True)
print("Done! Your MAC address for " + intf + " is " + mac)
