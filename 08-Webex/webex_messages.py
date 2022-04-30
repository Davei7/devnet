import json
import requests

# Get the token from the Webex account (REST API-Quick Start - Personal Token) [Expires in 12h]

token = ''

### GET TEAM ID ####
headers = {
    'Authorization':f'Bearer {token}',
    'Content-Type': 'application/json'
}

room_url = 'https://api.ciscospark.com/v1/rooms'

get_rooms = requests.get(room_url, headers=headers).json()

rooms = get_rooms['items']

for room in rooms:
    if room['name'] == 'Random Room':
        roomId = room['id']

### Post Message in the Room

msg_url = 'https://api.ciscospark.com/v1/messages'

msg_body = {
    "roomId": roomId,
    'text': 'ALERT: Interface GigaEthernet 0/1 on device Cisco Switch 9300 is DOWN!'
}

msg_response = requests.post(msg_url, headers=headers, data=json.dumps(msg_body)).json()