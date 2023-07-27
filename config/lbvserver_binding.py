import json
from json.decoder import JSONDecoder
import requests


def nitro_vserver_binding(l4_info, l4_vserver):
    url = f"https://{l4_info['ip']}/nitro/v1/config/lbvserver_binding/{l4_vserver}"
    # cookies = { 'Cookies' : f'NITRO_AUTH_TOKEN={token}'}
    lbvserver = []
    headers = { 'Content-Type':'application/json', "X-NITRO-USER":f"{l4_info['id']}", "X-NITRO-PASS":f"{l4_info['password']}" }
    response = requests.get(url, headers=headers, verify=False)
    result = response.json()
    lbvserver = result['lbvserver_binding']
    service = lbvserver[0]
    service_binding = service['lbvserver_service_binding']
    return service_binding