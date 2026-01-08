#!/usr/bin/env python3
# Use this program to obtain OAuth HTTP Token from ClearPass to reference
# in other API calls.  https://developer.arubanetworks.com/cppm/docs/getting-started-with-the-clearpass-policy-manager-api
import requests

def cppm_oauth2_token(
        cppm_ip,
        client_id,
        client_secret
):
    with requests.post(
        url=f'https://{cppm_ip}/api/oauth',
        headers={'Content-Type': 'application/json'},
        json={
            "grant_type": "client_credentials",
            "client_id": f"{client_id}",
            "client_secret": f"{client_secret}"
        },
        verify=False,
        timeout=20
    ) as res:
        return res.json()
