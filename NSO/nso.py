import requests
import json

from requests.api import head

url_base = 'https://sandbox-nso-1.cisco.com/api'
authentication = ("developer","Services4Ever")

headers = {'Accept':'application/vnd.yang.collection+json'}

response = requests.get(f'{url_base}/running', auth=authentication, headers=headers).json()

devices = response['collection']['tailf-ncs:device']

for device in devices:
    print(f"Name: {device['name']}")
    print(f"IP: {device['address']}")
    print(f"SSH Port: {device['port']}")
    print(f"Auth Group: {device['authgroup']}")
    print()
