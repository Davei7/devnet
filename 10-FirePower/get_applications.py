import requests
import json
import urllib3
import sys
from urllib3 import response

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set URL to login

url = 'https://fmcrestapisandbox.cisco.com'

login_url = '/api/fmc_platform/v1/auth/generatetoken'

headers = {'Content-Type':'application/json'}

username = ''
password = ''

login_response = requests.post(f'{url}{login_url}', auth=(username,password), verify=False)

response_headers = login_response.headers

token = response_headers.get('X-auth-access-token', default=None)

headers['X-auth-access-token'] = token

endpoint = ''

apps_url = f'/api/fmc_config/v1/domain/{endpoint}/object/applications'

app_response = requests.get(f'{url}{apps_url}',headers=headers, verify=False).json()

print(json.dumps(app_response, indent=2, sort_keys=True))
