from logging import _FormatStyle
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

policy_url = f'/api/fmc_config/v1/domain/{endpoint}/policy/accesspolicies'

payload = {
    "type": "AccessPolicy",
    "name": "AMP Policy",
    "description": "Test Policy",
    "defaultAction": {
        "intrusionPolicy":{
            "name": "Security Over Connectivity",
            "id": "abba9b63-bb10-4729-b901-2e2aa0f4491c",
            "type": "IntrusionPolicy"
        },
        "variableSet":{
            "name": "Default Set",
            "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
            "type": "VariableSet"
        },
        "type": "AccessPolicyDefaultAction",
        "logBegin": False,
        "logEnd": True,
        "sendEventsToFMC": True
    }
}

response_policy = requests.post(f'{url}{policy_url}',headers=headers, data=json.dumps(payload), verify=False).json()

print('*' * 10 + 'Policy Created' + '*' * 10)

print(json.dumps(response_policy, indent=2, sort_keys=True))

print('*' * 10 + 'Policy Created' + '*' * 10)

policyId = response_policy['id']

policy_url_mine = f'/api/fmc_config/v1/domain/{endpoint}/policy/accesspolicies/{policyId}'

# Rules to monitor files for Malware

rules_url = f'{policy_url_mine}/accessrules'

rules_payload = {
    "sendEventsToFMC": True,
    "action": "MONITOR",
    "enabled": True,
    "type": "AccessRule",
    "name": "Monitor Threat URLs",
    "logFiles": True,
    "logBegin": False,
    "logEnd": False,
    "variableSet": {
        "name": "Default Set",
        "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
        "type": "VariableSet"
    },
    "sourceNetwork":{
        "objects":[{
            "type": "NetworkGroup",
            "name": "IPv4-Private-All-RFC1918",
            "id": "15b12b14-dace-4117-b9d9-a9a7dcfa356f"
        }]
    },
    "filePolicy":{
        "name":"New Malware",
        "id": "59433a1e-f492-11e6-98fd-84ec1dfeed47",
        "type": "FilePolicy"
    }
}

rules_response = requests.post(f'{url}{rules_url}',headers=headers, data=json.dumps(rules_payload), verify=False).json()

print('*' * 10 + 'Rule Created' + '*' * 10)

print(json.dumps(rules_response, indent=2, sort_keys=True))

print('*' * 10 + 'Rule Created' + '*' * 10)

del_response = requests.delete(f'{url}{policy_url_mine}',headers=headers, verify=False).json()