import requests
import json
import re

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
        "input":"show cdp neighbors",
        "output_format":"json"
    }
}

#Get the right URL to the API of the Nexus device
url = f"https://{nexus['host']}/ins"

response = requests.post(url, data=json.dumps(payload), headers=headers, auth=(nexus['username'], nexus['password']), verify=False)

api_data = response.json()

print("*" * 75)
print(json.dumps(api_data, indent=2, sort_keys=True))

######################################### LOGIN WITH NX-API REST ########################################

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "Admin_1234!"
    }
  }
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()

##Get the Token for the session from the response
token=response['imdata'][0]['aaaLogin']['attributes']['token']

cookies={}
cookies['APIC-cookie']=token

counter = 0

# Getting the neighbor count from the command show cdp neighbors
nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']

while counter < nei_count:
  hostname = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
  local_int = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
  remote_int = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']

  payload_cycle = "{\r\n    \"l1PhysIf\": {\r\n        \"attributes\": {\r\n            \"descr\":\"Connected to "+hostname+" Remote if is " + remote_int + "\"\r\n        }\r\n    }\r\n}"

  counter += 1

  if local_int != 'mgmt0':
    int_name = str.lower(str(local_int[:3]))
    int_num = re.search(r'[1-9]/[1-9]*', local_int)
    int_url = "https://sbx-nxos-mgmt.cisco.com/api/mo/sys/intf/phys-["+int_name+str(int_num.group(0))+"].json"
    post_response = requests.post(int_url, data=json.dumps(payload_cycle), headers=headers, cookies=cookies, verify=False).json()

  print(post_response)








