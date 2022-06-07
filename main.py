#!/usr/bin/env python

import subprocess

interface = "wlan0"
new_mac = "00:11:22:11:33:11"

print(f"[+] Changing MAC address for {interface} to {new_mac}")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

