from dnacentersdk import api
import json

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com', username='devnetuser', password='Cisco123!')

##### Networks & Sites

sites = dna.topology.get_site_topology()

print(sites.response)

for site in sites.response.sites:
    if site.parentId == '27eb9050-63bf-4832-92a0-95796391a92b':
        print("*" * 25)
        print(f"Site Name: {site.name}")
        for child_sites in sites.response.sites:
            if child_sites in sites.response.sites:
                print(f"Child Name:  {child_sites.name}")
                for more_children in sites.response.sites:
                    if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
                        print(f"More Children: {more_children.name}")
        print("*" * 25)

# Print VLANs

vlans = dna.topology.get_vlan_details()
i = 1
for vlan in vlans.response:
    print(f"{i} Vlan: {vlan}")
    print("*" * 25)
    i+=1

print(f"There are {i} VLANs programmed in this DNA-Center!")
print("*" * 25)

# Print Topology Details (Device Types)

physical_topology = dna.topology.get_physical_topology()

for devices in physical_topology.response.nodes:
    print(f"Device: {devices.deviceType}")
    print("*" * 25)


