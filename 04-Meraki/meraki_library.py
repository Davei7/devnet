import meraki
import json

# Set Headers for Meraki (API-Key)
token = "efc3bed467e455a5a8fd51dcdefb2e20ce231442"

dashboard = meraki.DashboardAPI(token)

my_orgs = dashboard.organizations.getOrganizations()

# print(json.dumps(my_orgs, indent=2, sort_keys=True))

for org in my_orgs:
    if org['name'] == 'DevNet Sandbox':
        orgId = org['id']

my_networks = dashboard.organizations.getOrganizationNetworks(orgId)

# print(json.dumps(my_networks, indent=2, sort_keys=True))

for network in my_networks:
    if network['name'] == 'DNSMB2':
        netId = network['id']

my_clients = dashboard.networks.getNetworkClients(netId)

my_devices = dashboard.networks.getNetworkDevices(netId)

# if my_clients == []:
#     print("*" * 50)
#     print("There are no clients in this network!")
#     print("*" * 50)
# else:
#     print(json.dumps(my_clients, indent=2, sort_keys=True))

if my_devices == []:
    print("There are no devices in this network!")
else:
    print(json.dumps(my_devices, indent=2, sort_keys=True))
    for device in my_devices:
        if device['model'] == 'MS220-8P':
            serial_id = device['serial']
    

port_switch = dashboard.switch.getDeviceSwitchPorts(serial_id)

print(json.dumps(port_switch, indent=2, sort_keys=True))