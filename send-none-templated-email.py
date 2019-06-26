import http3
import json
import os
from pprint import pprint
import sys

# create contact via send in blue http interface
# https://api.sendinblue.com/v3/contacts
# body params
# email
json_file = sys.argv[1]


try:
    url = 'https://api.sendinblue.com/v3/smtp/email'
    sibkey = os.environ['SEND_IN_BLUE_KEY']
    headers = {'Accept': "application/json",
               'Content-Type': 'application/json',
               'api-key': sibkey}

    with open(json_file) as json_file:
        data = json.load(json_file)
        r = http3.post(url, headers=headers, json=data)
        pprint(r)
        pprint(r.json())

except Exception as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
