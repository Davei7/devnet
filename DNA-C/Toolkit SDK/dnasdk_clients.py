from dnacentersdk import api
import json
import time
import calendar

dna = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com', username='devnetuser', password='Cisco123!')

##### Clients & Health

epoch_timedate = calendar.timegm(time.gmtime())

client_health = dna.clients.get_overall_client_health(timestamp=str(epoch_timedate))

print(json.dumps(client_health.response, indent=2, sort_keys=True))

### Network health

site_health = dna.sites.get_site_health(timestamp=str(epoch_timedate))

print(json.dumps(site_health.response, indent=2, sort_keys=True))