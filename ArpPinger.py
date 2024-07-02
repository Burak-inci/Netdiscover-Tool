import argparse
import scapy.all as scapy

class ARPPing():

    def __init__(self):
        print("ARPPing has been initiated...")

    def get_user_input():
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ipaddress', type=str, help="You must enter your IP address")
        args = parser.parse_args()
        #print(args.ipaddress)

        if args.ipaddress != None:
            return args
        else:
            print("enter the ip address with the -i argument.")

    def arp_request(self,ip):
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet / arp_request_packet
        (answered_list, unanswered_list) = scapy.srp(combined_packet, timeout=1)
        answered_list.summary()

if __name__ == "__main__":
    arp_ping = ARPPing()
    user_input = arp_ping.get_user_input()
    arp_ping.arp_request(user_input.ipaddress) 