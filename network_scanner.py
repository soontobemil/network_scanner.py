#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcst = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcst, timeout=1) #sr = send and receive p=custom packet
    print(answered.summary())
    # print(answered)
scan("192.168.64.1/24")
