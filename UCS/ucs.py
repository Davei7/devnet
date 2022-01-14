from ucsmsdk.ucshandle import UcsHandle

ip_UCS = ""
username = ""
password = ""


handle = UcsHandle(ip_UCS, username, password)

handle.login()

# Organization Information

org = handle.query_classid(class_id = "orgOrg", hierarchy=True)

# Server Blade Info
servers = handle.query_classid("computeBlade")

for server in servers:
    print(server.dn, server.num_of_cpus, server.available_memory)

# Specify DN query
blade = handle.query_dn('sys/chassis-3/blade-1')

print(blade)

# Logout

handle.logout()