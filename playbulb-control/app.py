import os
import nmap
from time import sleep
from pybulb.bulb import Bulb

def run_app():

    playbulb_address = os.getenv('PLAYBULB_ADDRESS')
    devices_mac_addresses = os.getenv('DEVICES_MAC').split(',')

    bulb = Bulb(playbulb_address)
    nm = nmap.PortScanner()
    while(True):
        device_here = False
        scan = nm.scan(hosts='10.0.0.0/24', arguments='-sP')['scan']
        for host in scan:
            addresses = scan[host]['addresses']
            if ('mac' in addresses and addresses['mac'] in devices_mac_addresses):
                device_here = True

        if (device_here):
            not bulb.is_on() and bulb.on()
        else:
            bulb.is_on() and bulb.off()

        sleep(1)


