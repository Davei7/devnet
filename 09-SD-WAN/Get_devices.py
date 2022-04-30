import requests
import json
import urllib3
import sys
from urllib3 import response

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set URL to login

url = 'https://sandbox-sdwan-1.cisco.com/j_security_check'

login_body = {
    'j_username':'devnetuser',
    'j_password':'RG!_Yw919_83'
}

session = requests.session()

response = session.post(url, data=login_body, verify=False)

## Response returns 200 if accepts the connection
if not response.ok or response.text:
    print("Login Failure!")
    sys.exit(1)
else:
    print("Login OK!")

# Get Devices
url = "https://sandbox-sdwan-1.cisco.com/dataservice/device"

device_response = session.get(url, verify=False).json()['data']

for device in device_response:
    print(f"Hostname: {device['host-name']}")
    print(f"IP Address: {device['local-system-ip']}")
    print(f"Model: {device['device-model']}")
    print()

# Get Templates
url_templates = "https://sandbox-sdwan-1.cisco.com/dataservice/template/device"

template_response = session.get(url_templates, verify=False).json()['data']

print(template_response)