## Network Scanner

A simple Python-based network scanner that discovers active hosts on a local network using ARP requests.
The tool displays the IP and MAC address of every device that responds.

## Features

Scan a single IP address or an entire network range.
Fast ARP-based host discovery.
Displays IP and MAC addresses in a clean table.
Simple command-line interface.


## Requirements

Python 3.*

Linux (requires raw socket access)

Root privileges

Scapy

## Installation

git clone https://github.com/meedblg/network_scanner.git

cd network-scanner

sudo python3 network-scanner.py -r <IP_ADDRESS_OR_NETWORK>

or

sudo python3 network-scanner.py --range <IP_ADDRESS_OR_NETWORK>


## Examples

Scan a single host:

sudo python3 network-scanner.py -r 192.168.1.1

Scan an entire subnet:

sudo python3 network-scanner.py -r 192.168.1.0/24
