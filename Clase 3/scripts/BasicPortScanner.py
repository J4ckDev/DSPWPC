#!/usr/bin/python3

import nmap
from pprint import PrettyPrinter

nmap_port_scanner = nmap.PortScanner()

ip_to_scan = '172.17.0.2'

#ports_to_scan = '1-65535'
#ports_to_scan = '10, 20, 30, 44, 25'
ports_to_scan = '21'

aditional_parameters = "-sS"

scan_result = nmap_port_scanner.scan(ip_to_scan, ports_to_scan, aditional_parameters)

pretty_print = PrettyPrinter(depth=10)
pretty_print.pprint(scan_result)