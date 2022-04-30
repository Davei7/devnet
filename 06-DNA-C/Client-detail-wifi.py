import requests
import json


# Authentication with DNA-C
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

response = requests.post(url, auth=(user, password)).json()

token = response['Token']

# Get Client Health Stats

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-detail"

macAddress = '00:00:2A:01:00:2E'

querystring = {"timestamp": "",  "macAddress": macAddress}

headers = {
    'x-auth-token': token
}

response = requests.get(url, headers = headers, params=querystring).json()

device_details = response['topology']['nodes']

for device_detail in device_details:
    if device_detail['id'] == device_details[0]['id']:
        print(f"Client IP: {device_detail['ip']}")
        print(f"MAC: {device_detail['id']}")
        print(f"Health Score: {device_detail['healthScore']}")
        print()
    elif device_detail['id'] == device_details[0]['id']:
        print(f"Connected to: {device_detail['deviceType']}")
        print(f"WAP IP: {device_detail['ip']}")