import requests
import json

# Set up the connection parameters in a dictionary
router = {"host": "ios-xe-mgmt-latest.cisco.com", "port":"443",
            "username": "developer", "password" : "C1sco12345"}

#Set up the module in use
module = {"module": "Cisco-IOS-XE-interfaces-oper", "container": "interfaces", "leaf":"interface"}

# Set the URL
url = f"https://{router['host']}:{router['port']}/restconf/data/{module['module']}:{module['container']}/{module['leaf']}=GigabitEthernet2"

# Set REST API Headers
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.get(url, headers=headers, auth=(router['username'], router['password']), verify=False)

api_data = response.json()

# The next interaction will show the interface description
print("*" * 75)
print(api_data[module['module']+":"+module['leaf']]["description"])

print("*" * 75)
if api_data[module['module']+":"+module['leaf']]["admin-status"] == 'if-state-up':
    print("Interface is up!")
else:
    print("Interface is down!")