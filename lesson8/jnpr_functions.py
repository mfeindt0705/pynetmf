import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable

def check_connected(a_device):
    return a_device.connected


def gather_routes(a_device):
    route_entries = RouteTable(a_device)
    route_entries.get()
    return route_entries


def gather_arp_tables(a_device):
    arp_entries = ArpTable(a_device)
    arp_entries.get()
    return arp_entries


def print_output(a_device, arp_table, route_table):
    # print device host facts
    vdict = a_device.facts
    print(f"Model {vdict['model']} with hostname {vdict['hostname']}")
    print(f"Connected via port {a_device.port} with user {a_device.user}")

    # print arp cache entries
    print("")
    print("Device Arp cache entries : ")
    for mac in arp_table:
        print(f"MAC address {mac['mac_address']} for IP address {mac['ip_address']}")
    
    # print routing table entries
    print("")
    print("Device route table entries : ")
    for k in route_table.keys():
        vdict = dict(route_table[k].items())
        if vdict['nexthop']:
            next_hop_ip = vdict['nexthop']
        else:
            next_hop_ip = "LOCAL"
        print(f"Network {k} with next hop IP {next_hop_ip}")
    return None

