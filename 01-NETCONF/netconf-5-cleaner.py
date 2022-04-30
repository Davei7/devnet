from ncclient import manager
import xmltodict
import xml.dom.minidom
from router_info import router


netconf_filter = open("C:/Users/Davide Dias/Desktop/DevNet/Scripts/NETCONF_YANG/netconf-filter.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)    

    # Get the running config on the filtered out interface
    print("Connected!")
    interface_netconf= m.get(netconf_filter)
    print("Getting Running config")

    # XML for converting xml output to a python dictionary
    interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
    print('*' * 25 + 'Interface' + '*' * 25)
    print(interface_python)

    name = interface_python['interfaces']['interface']['name']
    print('*' * 25 + 'Name' + '*' * 25)
    print(name)

    ## Additional part of the script
    ## Parsing specific data of the RPC-Reply data
    config = interface_python["interfaces"]["interface"]
    op_state = interface_python["interfaces-state"]["interface"]

    print('*' * 75)
    print("Start")
    print(f"Name: {config['name']}")
    print(f"Description: {config['description']}")
    print(f"Packet In {op_state['statistics']['in-unicast-pkts']}")