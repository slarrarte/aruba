#!/usr/bin/env python3
# Aruba ClearPass Policy Manger - Update Static Host List for IoT Devices
import get_http_token, requests, json
from getpass import getpass
from pathlib import Path

requests.packages.urllib3.disable_warnings()

cppm_ip = '10.10.16.216'
cppm_api_endpoint = f'https://{cppm_ip}/api/static-host-list/3002' # 3002 is id of my test SSID
client_id = 'iot_static_host_list_updater'
client_secret = getpass('Client Secret: ') # API key

json_file_path = Path.home()/'Documents/python/aruba/static_host_list_file.json'

# Obtain OAuth token by parsing returned json payload
oauth_token = get_http_token.cppm_oauth2_token(
        cppm_ip,
        client_id,
        client_secret
    ) ["access_token"]

# GET Current Static Host List
with requests.get(
    url=cppm_api_endpoint,
    headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {oauth_token}'
    },
    verify=False,
    timeout=20
) as res:
    print(json.dumps(res.json(), indent=2))

# You must PATCH the new, complete host database.  If you try to just PATCH one,
# it will act as a PUT and delete all existing entries.

# # PATCH new MAC address in static host list
# Extract json
with open(json_file_path) as json_contents:
    json_data = json.load(json_contents)

# HTTP PATCH starts here
with requests.patch(
    url=cppm_api_endpoint,
    headers={
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {oauth_token}'
    },
    verify=False,
    timeout=20,
    json=json_data
) as patch_res:
    print(res.status_code)
