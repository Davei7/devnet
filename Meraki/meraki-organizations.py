import requests
import json

# Set the URL
url = "https://dashboard.meraki.com/api/v0/organizations"

# Set Headers for Meraki (API-Key)
headers = {
  'X-Cisco-Meraki-API-Key':"efc3bed467e455a5a8fd51dcdefb2e20ce231442"
}

response = requests.get(url, headers=headers).json()

print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
    if response_org['name'] == 'DevNet Sandbox':
        orgId = response_org['id']

print("\n*" * 50)
print(orgId)
print("*" * 50)