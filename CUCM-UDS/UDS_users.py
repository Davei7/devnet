import requests
import xml.dom.minidom
import xmltodict
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#### For CUCM 11.5 #######
url = "https://10.10.20.1/cucm-uds"

endpoint = 'users'

users_url = f'{url}/{endpoint}'

headers = {
    'Accept':'application/xml',
    'Content-Type':'application/xml'
}

user = 'administrator'
password = 'ciscopsdt'

response = requests.get(users_url, auth=(user, password), verify=False)

# Pretty up the XML Response
tree = xml.dom.minidom.parseString(response.text)
pretty = tree.toprettyxml()

# Convert to Python Dict
xmldata = xmltodict.parse(pretty)

users = xmldata['users']['user']

for user in users:
    print(f"{user['lastName']} {user['firstName']}")
    print(f"ID: {user['id']}")
    print("*" * 25)