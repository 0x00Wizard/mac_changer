#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",
                  help="interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac",
                  help="New MAC address")

parser.parse_args()


interface = input("Enter interface > ")
new_mac = "00:11:22:11:33:11"

print(f"[+] Changing MAC address for {interface} to {new_mac}")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

