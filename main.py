#!/usr/bin/env python

import subprocess

interface = "wlan0"

subprocess.call(f"ifconfig {interface} down")
subprocess.call(f"ifconfig {interface} down")
subprocess.call(f"ifconfig {interface} down")