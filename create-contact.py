import http3
import os
from pprint import pprint
import sys


# create contact via send in blue http interface
# https://api.sendinblue.com/v3/contacts
# body params
# email
email = sys.argv[1]


try:
    url = 'https://api.sendinblue.com/v3/contacts'
    sibkey = os.environ['SEND_IN_BLUE_KEY']
    headers = {'api-key': sibkey}
    data = {'email': email}
    r = http3.post(url, headers=headers, json=data)
    pprint(r)
    pprint(r.json())

except Exception as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
