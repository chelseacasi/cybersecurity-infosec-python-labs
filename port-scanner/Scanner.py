#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<------------------------>")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\n Please enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP Scan
                3)COmprehensive Scan \n""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -T4 --host-timeout 60s')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr]:
        print("Open Ports: ", list(scanner[ip_addr]['tcp'].keys()))
    else:
        print("No open TCP ports found")

elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU -T4 --host-timeout 60s')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'udp' in scanner[ip_addr]:
        print("Open Ports: ", list(scanner[ip_addr]['udp'].keys()))
    else:
        print("No open UDP ports found")

elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -A -T4 --host-timeout 3m')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr]:
        print("Open Ports: ", list(scanner[ip_addr]['tcp'].keys()))
    else:
        print("No open TCP ports found")
else:
    print("Please enter a valid option")
