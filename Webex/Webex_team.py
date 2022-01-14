import json
import requests

# Get the token from the Webex account (REST API-Quick Start - Personal Token) [Expires in 12h]

token = ''

### Create a TEAM ####

url = 'https://api.ciscospark.com/v1/teams'
headers = {
    'Authorization':f'Bearer {token}',
    'Content-Type': 'application/json'
}

body = { "name":"Awesome Team!"}

post_response = requests.post(url, headers=headers, data=json.dumps(body)).json()

print(post_response)

get_response = requests.get(url, headers=headers).json()

teams = get_response['items']

x = 1
for team in teams:
    print(f"Team {x}: {team['name']}")
    x+=1