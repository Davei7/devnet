from acitoolkit.acitoolkit import *
import json

# See capabilities

url = "https://sandboxapicdc.cisco.com"
user = 'admin'
pw = '!v3G@!4@Y'

# Create the session object
session = Session(url, user, pw)

# Login to the session
session.login()

# Get a list of all the tenants
tenants = Tenant.get(session)

for tenant in tenants:
    print('*' * 25)
    print("Name: " + tenant.name)
    print("Description: " + tenant.descr)
    print('*' * 25)
    print()

# Create a new Tenant
new_tenant = Tenant("Zeus_Tenant")

# Create the application profile & the EPG
new_application_pro = AppProfile('Gaia_App', new_tenant)
new_endpoint_group = EPG('Kronos_EPG', new_application_pro)

# Create the L3 Namespace
new_context = Context('Hades_VRF', new_tenant)
new_bridge_domain = BridgeDomain('Ares_BD', new_tenant)

# Associate the BD with the L3 Namespace
new_bridge_domain.add_context(new_context)
new_endpoint_group.add_bd(new_bridge_domain)

# Tenant is created successfully
print(new_tenant.get_url())
print(new_tenant.get_json())

response = session.push_to_apic(new_tenant.get_url(), data=new_tenant.get_json()).json()

print(json.dumps(response, indent=2, sort_keys=True))

# Get the Name and the description of the Tenant Created

tenants = Tenant.get(session)

for tenant in tenants:
    if tenant.name == 'Zeus_Tenant':
        print('*' * 25)
        print("Name: " + tenant.name)
        print("Description: " + tenant.descr)
        print('*' * 25)
        print()

# # Delete the Tenant created
new_tenant.mark_as_deleted()
session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())