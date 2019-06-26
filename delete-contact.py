import http3
import os
from pprint import pprint
import sys


# create contact via send in blue http interface
# https://api.sendinblue.com/v3/contacts
# body params
# email

# email = 'fred@test.com'
email = sys.argv[1]


try:
    sibkey = os.environ['SEND_IN_BLUE_KEY']
    url = 'https://api.sendinblue.com/v3/contacts/'+email
    headers = {'api-key': sibkey}
    r = http3.delete(url, headers=headers)
    pprint(r)

except Exception as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
