import requests
import json

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

#url_put = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/97].json"

url_get = "https://sbx-nxos-mgmt.cisco.com/api/node/class/l2BD.json?"

get_response = requests.request("GET", url_get, headers=headers, cookies=cookies, verify=False).json() 

#payload = "{\r\n    \"l1PhysIf\": {\r\n        \"attributes\": {\r\n            \"descr\":\"Default VLAN\"\r\n        }\r\n    }\r\n}"

#put_response = requests.request("PUT", url, data=payload, cookies=cookies, verify=False).json() 

print(get_response)