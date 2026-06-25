import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('--r','-r','--range', dest="ip_address", help="This Option For ip address Or Network Range To scan")
    options, arguments = parser.parse_args()

    if not options.ip_address:
        parser.error("[*] Please Spicify an Ip address Or Network Range To scan")
        exit()

    return options

# creating ARP request
def scan(ip_address):
    arp_request = scapy.ARP(pdst=ip_address)
    arp_prodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = arp_prodcast/arp_request
    answerd = scapy.srp(request, timeout=1, verbose=False)[0]
    clients_list = []

    for ans in answerd:
        clients_dict = {"ip":ans[1].psrc, "mac":ans[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

#display the clients ip's and mac addresses
def display_clients(clients):
    print(f'{"IP":<30}MAC Address')
    print("-" * 47)

    for client in clients:
        print(f'{client["ip"]:<30}{client["mac"]}')

options =  get_arguments()
clients_list =  scan(options.ip_address)
display_clients(clients_list)
















