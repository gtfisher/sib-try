import http3
import os
from pprint import pprint

# create contact via send in blue http interface
# https://api.sendinblue.com/v3/contacts
# body params
# email


try:
    sibkey = os.environ['SEND_IN_BLUE_KEY']
    url = 'https://api.sendinblue.com/v3/contacts'
    headers = {'api-key': sibkey}
    r = http3.get(url, headers=headers)
    pprint(r)
    pprint(r.json())

except Exception as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
