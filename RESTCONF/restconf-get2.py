import requests
import json

# Set up the connection parameters in a dictionary
router = {"host": "ios-xe-mgmt-latest.cisco.com", "port":"443",
            "username": "developer", "password" : "C1sco12345"}

#The port for RESTCONF should be 9443 not 443 but the device is not accepting 9443 connections

#Set up the module, container and leaf in use
module = {"module": "Cisco-IOS-XE-interfaces-oper", "container": "interfaces", "leaf":"interface"}

# Set the URL
url = f"https://{router['host']}:{router['port']}/restconf/data/{module['module']}:{module['container']}"

# Set REST API Headers
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.get(url, headers=headers, auth=(router['username'], router['password']), verify=False)

api_data = response.json()

# The next loop will show all the names of the interface available in the network device 
# It also verifies if the interfaces are up or down
print("*" * 75)
for i in api_data[module['module']+":"+module['container']][module['leaf']]:
    print(i['name'])
    if i["admin-status"] == 'if-state-up':
      print("Interface is up!")
    else:
      print("Interface is down!")
    print("*" * 75)
