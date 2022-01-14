import requests
import json

# Set up the connection parameters in a dictionary
nexus = {"host": "sandbox-nxos-1.cisco.com",
            "username": "admin", "password" : "Admin_1234!"}

# Set Headers
headers = {
  'Content-Type': 'application/json'
}

#Set the payload
payload = {
    "ins_api": {
        "version": "1.0",
        "type":"cli_show",
        "chunk":"0",
        "sid":"1",
        "input":"show version",
        "output_format":"json"
    }
}

#Get the right URL to the API of the Nexus device
url = f"https://{nexus['host']}/ins"

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=(nexus['username'], nexus['password']), verify=False)

api_data = response.json()

print("*" * 75)
print(json.dumps(api_data, indent=2, sort_keys=True))
