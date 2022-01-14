import json
import requests

# Get the token from the Webex account (REST API-Quick Start - Personal Token) [Expires in 12h]

token = ''

### GET TEAM ID ####

url_teams = 'https://api.ciscospark.com/v1/teams'
headers = {
    'Authorization':f'Bearer {token}',
    'Content-Type': 'application/json'
}

get_response = requests.get(url_teams, headers=headers).json()

teams = get_response['items']

for team in teams:
    if team['name'] == 'Awesome Team!':
        teamId = team['id']

### Create a ROOM (Child of TEAM)

room_url = 'https://api.ciscospark.com/v1/rooms'

room_body = {
    "title" : "Random Room",
    "teamId": teamId
}

post_response = requests.post(room_url, headers=headers, data=json.dumps(room_body)).json()

get_rooms = requests.get(room_url, headers=headers).json()

rooms = get_rooms['items']

x = 1
for room in rooms:
    print(f"Room {x}: {room['name']}")
    x+=1