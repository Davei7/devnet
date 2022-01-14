import requests
import json
import urllib3
import sys
from urllib3 import response

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set URL to login

ip_asa = '' 

url = f'https://{ip_asa}/api/routing/static'

headers = {'Content-Type':'application/json', 'Accept':'application/json'}

username = ''
password = ''

get_response = requests.get(url, auth=(username,password), verify=False).json()['items']

print(json.dumps(get_response, indent=2, sort_keys=True))