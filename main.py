#!/usr/bin/env python

import subprocess
import optparse
import re


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="New MAC address")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a NEW MAC, use --help for more info")

    return options


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_args()


# change_mac(options.interface, options.new_mac)
def get_mac_address(interface, ):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search:
        print(mac_address_search.group(0))

    else:
        print("[-] Could not find MAC address.")
