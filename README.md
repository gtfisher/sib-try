# sib-try

Repo to expriment with SendInBlue Rest api

install dependencies with: `pip install -r requirements.txt`

you will need a send in blue account and a V3 api key

to get your key see [sind in blue accout link](https://account.sendinblue.com/advanced/api)

The the code references SEND_IN_BLUE_KEY environment variable that should point to your key

To use the replace the representative data with live email addresses etc

Commands

* list contacts `python get-contact.py`
* create contact `python create-contact.py <email-address>`
* delete contact `python delete-contact.py <email-address>`
* send email `python send-none-templated-email.py <jsonfile.json>`



