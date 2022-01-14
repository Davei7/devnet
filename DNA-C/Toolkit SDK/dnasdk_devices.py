from dnacentersdk import api
import json

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com', username='devnetuser', password='Cisco123!')

##### Devices

devices = dna.devices.get_device_list()

for device in devices.response:
    print(f"Type: {device.type}")
    print(f"Hostname: {device.hostname}")
    print(f"IP: {device.managementIpAddress}")
    print(f"ID: {device.id}")
    print()


#### Get specific device by ID

device_id = dna.devices.get_device_by_id('f16955ae-c349-47e9-8e8f-9b62104ab604')

print(json.dumps(device_id.response, indent=2, sort_keys=True))