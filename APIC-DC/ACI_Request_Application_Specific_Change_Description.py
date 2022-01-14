import json
import requests

### Login URL to get Token ###
url_login = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes":{
            "name":"admin",
            "pwd":"!v3G@!4@Y"
        }
    }
}

headers = {
    'Content-Type':"application/json"
}

response = requests.post(url_login, data=json.dumps(payload), headers=headers, verify=False).json()

### Parse token & set cookie ###
token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

### Get Applications ###

url_application = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-Heroes/ap-PowerABYF.json"

headers = {
    'cache-control': "no-cache"
}

#get_response = requests.get(url_application, headers=headers, cookies=cookie, verify=False).json()

#print(json.dumps(get_response, indent=2, sort_keys=True))

### Change the description ###

payload_descr = {
    "fvAp": {
        "attributes": {
            "descr":"",
            "dn":"uni/tn-Heroes/ap-PowerABYF"
        }
    }
}

post_response = requests.post(url_application, cookies=cookie, headers=headers, verify=False, data=json.dumps(payload_descr)).json()

print(json.dumps(post_response, indent=2, sort_keys=True))

get_response = requests.get(url_application, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2, sort_keys=True))