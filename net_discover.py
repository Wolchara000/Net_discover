#!/usr/bin/env python3

import scapy.all as scapy
from optparse import OptionParser


def get_args():
    # Parser
    parser = OptionParser()
    parser.add_option("-t", "--target", dest="targ", help="Specify the target or range in format IP/mask", metavar="TARGET")
    (options, arguments) = parser.parse_args()
    if not options.targ:
        parser.error("[-] Targets were not specified. Use -h for help.")
    return options


def ipasker(ip):
    # ARP request sender
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    return answered_list


def printer(answered_list):
    # Prints header
    print("IP\t\t\tMAC address\t\t\tSTATUS")
    print("--------------------------------------------------------------------")
    # Creating a List of Dictionaries
    clients_list = []
    for element in answered_list:
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        clients_list.append(client_dict)
    # Printing results
    if not clients_list:
        print("NO ACTIVE HOSTS on this search arguments. Use -h for help.")
    for client in clients_list:
        print(client["ip"]+"\t\t"+client["mac"]+"\t\tHOST IS UP")


# Main Program
# Disclaimer
print("############### Simple Net_Discover by Wolchara000 ###############")
ip = get_args()
scan = ipasker(ip.targ)
printer(scan)
