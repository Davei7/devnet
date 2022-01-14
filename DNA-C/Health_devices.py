import requests
import json


# Authentication with DNA-C
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

response = requests.post(url, auth=(user, password)).json()

token = response['Token']

# Get Client Health Stats

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health"

querystring = {"timestamp": ""}

headers = {
    'x-auth-token': token
}

response = requests.get(url, headers = headers, params=querystring).json()

print(f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")

scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == 'WIRELESS':
        print(f"Wireless Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")
        