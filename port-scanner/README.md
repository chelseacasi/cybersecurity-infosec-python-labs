Nmap Port Scanner

A simple nmap automation tool written in Python using the python-nmap library. It asks for a target IP address and a scan type, runs the scan, and prints the host status and the open ports it finds.

Files
Scanner.py - the interactive scanner
Scan types
Option	Scan	Nmap flags used	What it does
1	SYN ACK Scan	-v -sS -T4 --host-timeout 60s	Fast TCP scan of ports 1-1024
2	UDP Scan	-v -sU -T4 --host-timeout 60s	UDP scan of ports 1-1024 (slow by nature)
3	Comprehensive Scan	-v -sS -A -T4 --host-timeout 3m	TCP scan plus version detection, default scripts and OS detection
What the flags mean
-v - verbose output
-sS - SYN scan (TCP). Needs root.
-sU - UDP scan. Needs root.
-A - aggressive scan: turns on version detection (-sV), default scripts (-sC), OS detection (-O) and traceroute
-T4 - scan speed. Ranges from -T0 (slowest) to -T5 (fastest). -T4 is a good fast default on a lab network.
--host-timeout 60s - give up on a host after 60 seconds so the script does not hang on a host that never answers
Requirements
Linux (written and tested on Kali Linux in VMware)
Python 3
The nmap program
The python-nmap library
Installation
1. Install nmap
sudo apt install nmap
2. Install python-nmap

Newer Kali versions block pip install on the system Python ("externally-managed-environment" error). Use one of these:

Option A: apt (easiest)

sudo apt install python3-nmap

Option B: virtual environment (best practice)

python3 -m venv ~/venv
source ~/venv/bin/activate
pip install python-nmap
How to run
1. Find the IP address of the machine you want to scan

On Linux, run:

ip a

On Windows, run:

ipconfig

Look for the inet (Linux) or IPv4 Address (Windows) line, for example 192.168.1.50. Ignore 172.17.x.x addresses, which belong to Docker's internal network.

To test the scanner on your own machine, you can use 127.0.0.1.

2. Check that the target is reachable
ping 192.168.x.x

Replace 192.168.x.x with your own target's IP address.

3. Run the scanner with sudo

SYN, UDP and OS detection scans need root privileges:

sudo python3 Scanner.py

If you installed python-nmap inside a virtual environment, sudo python3 will not see it. Use the venv's Python instead:

sudo ~/venv/bin/python Scanner.py
4. Enter the target IP and choose a scan
Please enter the IP address you want to scan: 192.168.x.x

Please enter the type of scan you want to run
    1) SYN ACK Scan
    2) UDP Scan
    3) Comprehensive Scan

Type 1, 2 or 3 and press Enter. The IP address is typed in while the script runs, so no IP addresses are stored in the code.

5. Read the output

The script prints:

The nmap version
The scan info (scan method and port range)
Ip Status: - whether the host is up
The protocols found (tcp or udp)
Open Ports: - a list of open port numbers, or a message that none were found
Testing that it works

If your scan finds nothing, give it something to find.

Open a TCP port (web server on port 80):

sudo python3 -m http.server 80

Scan the machine's 192.168.x.x IP (or 127.0.0.1) with option 1. You should see Open Ports: [80].

Open a UDP port (port 5000):

nc -u -l -p 5000

Then scan with option 2.

Troubleshooting
Script hangs and never finishes: the IP is wrong or unreachable. Check for typos (for example 192.186... instead of 192.168...), and check that ping works first. Press Ctrl+C to stop it.
KeyError: 'tcp': the host is up but has no open TCP ports in the scanned range. Newer versions of the script check for this and print "No open TCP ports found" instead.
KeyError on the IP address: the host is down or not reachable, so nmap returned no result for it.
UDP scan returns an empty list ([]): this is normal. UDP scans are slow (many systems rate-limit the replies), closed ports are not listed, and firewalls often drop UDP silently. Scan a few ports (for example 53,123,161) and raise the timeout (--host-timeout 3m) for better results.
unrecognized option '-0': the OS detection flag is a capital letter O (-O), not a zero. With -A you do not need to add it separately.
requires root privileges: run the script with sudo.
ModuleNotFoundError: No module named 'nmap': python-nmap is not installed for the Python you are running. See the installation section.
Windows targets show no open ports: Windows Firewall usually filters scans. Ports will appear filtered or not at all.
Legal note

For learning only. Only scan machines you own or have explicit permission to test, such as your own VM or lab network. Scanning other people's systems without permission may be illegal.
