import signal
import requests
import json
import random
from abc import ABC, abstractmethod

TIMEOUT = 5

class tenant_api(ABC):

    @abstractmethod
    def __init__(self, url: str, headers: dict, payload: dict):
        pass

    @abstractmethod
    def get_tenants(self) -> dict:
        pass


class tenant_call(tenant_api):

    def __init__(self, url, headers, payload):
        self.url = url
        self.headers = headers
        self.data = payload

    def get_tenants(self):
        try:
            return requests.request("GET", url=self.url, headers=self.headers, data=self.data) if not None else None
        except:
            return None

class dealer_api(ABC):

    @abstractmethod
    def __init__(self, url, headers, payload) -> None:
        pass

    def get_dealerId(self)->list:
        pass


class dealer_call(dealer_api):

    def __init__(self, url, headers, payload):
        self.url = url
        self.headers = headers
        self.data = payload

    def get_dealerId(self):
        try:
            return requests.request("GET", url=self.url, headers=self.headers, data=self.data)
        except:
            return None


def add_scanner(tenant_id,dealer_id,mac_id,ip,resolution,color_mode,duplex_mode,model,scanner_driver_type,i,is_shared,shared_dealer_ids):

    url = "https://stageapp.tekioncloud.xyz/api/scanner-mgmt/u/v1/scanners/add-scanner"

    payload_dump = {
      "tenantId": tenant_id,
      "dealerId": dealer_id,
      "macId": mac_id,
      "displayName": f"test-scanner-{i}",
      "ipAddress": ip,
      "make": "Brother",
      "model": model,
      "group-id": "groupId-1",
      "scannerDriverType": scanner_driver_type,
      "shared": is_shared,
      "dealerIds": shared_dealer_ids,
      "options": {
        "colorMode": color_mode,
        "resolution": resolution,
        "duplex": duplex_mode
      }
    }

    payload = json.dumps(payload_dump)
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.json()['status'] == 200:
            print(response.json())
        else:
            print(json.dumps(payload_dump, indent=4, sort_keys=False))
    except Exception as e:
        print(e)

def generate_macId(m):
    while True:
        mac_id = ':'.join(format(random.randint(0,255), '02x') for i in range(6))
        if mac_id not in m:
            break
    return mac_id

def generate_ip(a):
    ip='10.101.'
    while True:
        ip += '.'.join(str(random.randint(0,255)) for i in range(2))
        if ip not in a:
            break
    return ip

def create_scanner_record(n, tenant_dict):
    scanner_driver_type_list = ["SANE", "TWAIN", "WIA"]
    resolution_options = [100,200,300]
    color_mode_options = ["COLOR","B_W"]
    duplex_mode_options = [True,False]
    model_options = ["ADS-3600W","ADS-1500W","ADS-1250W","ADS-2200","ADS-2700W"]

    import fetch_scanner_records as f
    records = f.api(f.url, f.headers, f.payload).get_records()
    ipAdrs, macIds = [], []
    if records is not None:
        ipAdrs = [i['ipAddress'] for i in records["data"]["hits"]]
        macIds = [i['macId'] for i in records["data"]["hits"]]

    for i in range(n):
        tenant_id = random.choice(list(tenant_dict.keys()))
        corresponding_dealers = tenant_dict.get(tenant_id)
        dealer_id = random.choice(corresponding_dealers)

        shared_dealer_ids = [i for i in corresponding_dealers if i != dealer_id]
        is_shared = False
        if shared_dealer_ids:
            is_shared = True

        mac_id= generate_macId(macIds)
        ip = generate_ip(ipAdrs)
        resolution = random.choice(resolution_options)
        color_mode = random.choice(color_mode_options)
        duplex_mode = random.choice(duplex_mode_options)
        scanner_driver_type = random.choice(scanner_driver_type_list)
        model = random.choice(model_options)
        add_scanner(tenant_id, dealer_id, mac_id, ip, resolution, color_mode, duplex_mode, model, scanner_driver_type, i,is_shared,shared_dealer_ids)



if __name__ == '__main__':
    tenant_url = "https://stageapp.tekioncloud.xyz/api/adminservice/u/globalSettings/tenants"
    payload={}
    headers = {
    'Content-Type': 'application/json',
    'origin': 'https://stageapp.tekioncloud.xyz',
    'authority': 'stageapp.tekioncloud.xyz',
    'dealerid': '4',
    'tek-siteid': '-1_4',
    'sec-gpc': '1',
    'userid': '32b87bf1-1361-4c29-953f-871580c4b36d',
    'tekion-api-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6ImdhdXJhdnByaW50aW5nIiwibmFtZSI6ImdhdXJhdnByaW50aW5nQG1haWxpbmF0b3IuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzJiMTZmMzNiYjY1YjNjYzZmOTc1MjI2MDlmMjk0ZDgyP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZ2EucG5nIiwidXBkYXRlZF9hdCI6IjIwMjEtMDgtMzFUMDU6NDE6MDIuODM0WiIsImVtYWlsIjoiZ2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly90ZWtpb24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzUwMmQ5NmIzYTYzMDA2OGE4OGYyOCIsImF1ZCI6ImxNU3pxYlM3OEVua1hwNXJoWTdaZFZkZHMwQVh2QzRSIiwiaWF0IjoxNjMwMzg4NDYzLCJleHAiOjE2MzA0MjQ0NjN9.ZSp-jz7Ncvy2dTiNixyZnik3nGMlcog17mvQkRH3PK5OOMWSH6qI30W98e4Mnb86Cp-_YREeDlVjiiLGqmbtmKj3MDq1G6j0b3JKpWhfbojQXPgJ5Q46uy5N92QL40q_v-5E_po6IaqCDU9sX10N5g2o38GM6tnmHcn1fR5NanWke4ohFG9JW0b1lHeslDBvqfb-dAMcv3p8BSY6-ltO9lR4S4k7LB3QhXOgVWqnLgIpXAjr-PPWc38M9hNlhJcNzLX873WLLGzqfBEbmb4vWtHx65y-dnnRZNISC8W5QcFKFt_38dRF-LYM8uWjlBZGQVoukSgC6EJNdRxK787vmg',
    'tenantname': 'stg-cacargroup',
    'traceparent': '00-5c456af4dfa3c1a5f78622e829e21909-fede49f6106e391a-01',
    'original-userid': 'null',
    'dealerid': '4',
    'roleid': '4_Controller',
    'tenantid': 'undefined'
    }

    tenants = tenant_call(tenant_url, headers, payload).get_tenants()
    tenants = tenants.json()['data']
    fDict = {}
    if tenants is not None:
        [fDict.update({tenant:[k['dealerId'] for k in dealer_call(url = f"https://stageapp.tekioncloud.xyz/api/adminservice/u/globalSettings/tenants/{tenant}/dealers", headers=headers, payload=payload).get_dealerId().json()['data']]}) for tenant in tenants]

    times = 0
    first = 1
    try:
        while True:
            signal.alarm(6)
            if first == 1:
                times = int(input("\n[*] you have 5 seconds to input the create count...\n"))
                first = 0
            else:
                times = int(input("\n[*]Want to add more? you have 5 seconds to feed input...\n"))
            signal.alarm(0)
            if times == 0:
                print("[*] Aborting the process.\n")
                break
            elif times<0:
                print("[*] Enter a valid +ve no")
            else:
                create_scanner_record(times, fDict)
    except Exception as err:
        print(err, "try changing the code.")
