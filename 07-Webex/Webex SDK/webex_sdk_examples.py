from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='')

### Get Team info
teams = api.teams.list()

for team in teams:
    print(team)
    if getattr(team, 'name')!= 'Awesome Team!':
        create_team = api.teams.create('Awesome Team')
        teamId = getattr(create_team, 'id')
    else:
        teamId = team.id

### People
print(api.people.me())
print(api.people.list())

api.people.create(emails='djmxdias@gmail.com', displayName='Luis Dias', firstName='Luis', lastName='Dias', roles='')

### Roles

roles = api.roles.list()

for role in roles:
    print(role)

### Rooms

rooms = api.rooms.list()
evaluator = False
for room in rooms:
    if room.title == 'Random Room':
        evaluator = True
        roomId = room.id

if evaluator == False:
    new_room = api.rooms.create('Random Room', teamId=teamId)
    roomId = new_room.id

#### Messages

api.messages.create(roomId, text='Using the SDK')

### Cleanup

# for room in rooms:
#     if getattr(room, 'title') == 'Random Room':
#         api.rooms.delete(getattr(room, 'id'))

# for team in teams:
#     if getattr(team, 'name') == 'Awesome Team!':
#         api.teams.delete(getattr(team, 'id'))

