TCP Client and Server

A basic TCP server and client written in Python using the socket module. The server waits for a connection, and the client connects to it and prints the message it receives.

Files
TCPserver.py - listens on a port and sends a message to each client that connects
tcpclient.py - connects to the server and prints the reply
Requirements
Python 3
Two terminals (or two machines on the same network, such as a Kali VM and your PC)
How to run
1. Find the server's IP address

On the machine that will run the server, run:

ip a

(on Windows, use ipconfig). Look for the inet line, for example 192.168.1.50. That is the server's IP address.

If the server and client run on the same machine, you can just use 127.0.0.1.

2. Set your own IP in the client

Open tcpclient.py and replace the placeholder with the server's IP address you found in step 1:

python
host = '127.0.0.1'   # replace with the server's IP address
port = 9999          # must match the port in TCPserver.py
3. Check the server settings

In TCPserver.py, make sure the server listens on all interfaces and uses the same port as the client:

python
host = '0.0.0.0'
port = 9999

Ports below 1024 need root on Linux, so use a port like 9999.

4. Start the server first
python3 TCPserver.py

Wait until it is listening.

5. Run the client

In a second terminal:

python3 tcpclient.py

The client should print the message sent by the server.

6. Stop the server

Press Ctrl+C in the server's terminal.

Troubleshooting
Connection refused: the server is not running, or the IP or port in the client does not match the server.
Works on the same machine but not from another one: the server must listen on 0.0.0.0 (not localhost), and a VM should use Bridged networking so other devices can reach it.
Address already in use: the old server is still running. Stop it with Ctrl+C, or wait a few seconds and try again.
Note

For learning only. Run this on your own machines and your own lab network.
