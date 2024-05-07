import requests

login = {
    "login":
    {
        "username":"nsroot",
        "password":"nsroot",
        "timeout" : "3600"
    }    
}

# param = { "X-NITRO-USER":"nsroot", "X-NITRO-PASS":"wkdb1100" }    


def nitro_login():
    url = 'https://10.10.10.10/nitro/v1/config/login'
    # headers = {'Content-Type' : 'application/vnd.com.citrix.netscaler.login+json'}
    headers = {'Content-Type':'application/json' }
    response = requests.post(url, json=login, headers=headers, verify=False)
    result = response.json()
    result2 = response.headers
    print(result)
    token = result['sessionid']
    print(token)
    return token
