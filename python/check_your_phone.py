#!/usr/bin/env python

from twilio.rest import Client 

# returns 'None' if the key doesn't exist
account = 'TWILIO_ACCOUNT_SID'
token = 'TWILIO_ACCOUNT_TOKEN'

# information
my_number = '+xxx'
forgot_humber = '+xxx'
client = Client(account, token)

client.messages.create(
    to=forgot_humber,
    from_=my_number,
    body="Don't forget me!!"
)
