import json
from json.decoder import JSONDecoder
import requests


def nitro_vserver(l4_info):
    url = f"https://{l4_info['ip']}/nitro/v1/config/lbvserver"
    # cookies = { 'Cookies' : f'NITRO_AUTH_TOKEN={token}'}
    headers = { 'Content-Type':'application/json', "X-NITRO-USER":f"{l4_info['id']}", "X-NITRO-PASS":f"{l4_info['password']}" }
    response = requests.get(url, headers=headers, verify=False)
    result = response.json()
    lbvservers = result['lbvserver']
    vservers_info = []
    for lbvserver in lbvservers:
        name = lbvserver["name"]
        vip = lbvserver['ipv46']
        vport = lbvserver['port']
        protocol = lbvserver['servicetype']
        lbmethod = lbvserver['lbmethod']
        state = lbvserver['curstate']
        vserver_data = {
            'name' : name.replace(',', ' '),
            'vip' : vip.replace(',', ' '),
            'vport' : vport,
            'protocol' : protocol.replace(',', ' '),
            'lbmethod' : lbmethod.replace(',', ' '),
            'state' : state.replace(',', ' ')
        }
        vservers_info.append(vserver_data)
    return vservers_info
