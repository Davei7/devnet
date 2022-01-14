from ncclient import manager
import xmltodict
import xml.dom.minidom

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port":"830",
            "username": "developer", "password" : "C1sco12345"}

netconf_filter = """
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
    	        <name>GigabitEthernet2</name>
            </interface>
        </interfaces>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet2</name>
            </interface>
        </interfaces-state>
    </filter>
"""

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