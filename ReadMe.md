
# This is a repo I use to send automated messages

main.py sends WhatsApp messages using selenium. 
notif_enabled_code enables sending text messages using twilio. (I used it for when my code crashes)

First you might need to install twilio and set up your account to get a phone number.
```
pip install twilio
```

To run notif_enabled_code:
```
python notif_enabled_code.py +1from_number +1to_number SID auth_token
```

Replace +1from_number with your twilio number  
Replace +1to_number with the number that has to recieve the text message.  
Replace SID with your Twilio account SID.  
Replace auth_toke with your Twilio account auth token

Output: 
Sent from your Twilio account - Your Pytorch code has crashed with the following error: name 'paes' is not defined


Good Luck!
