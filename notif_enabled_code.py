import sys
from twilio.rest import Client
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('phone_number_1', help='The first phone number')
    parser.add_argument('phone_number_2', help='The second phone number')
    parser.add_argument('SID', help='The twilio account SID')
    parser.add_argument('auth_token', help='The twilio Authentication token (keep secret)')


    args = parser.parse_args()

    from_number = args.phone_number_1 #this is twilio number
    to_number = args.phone_number_2

    print(from_number)
    print(to_number)

    account_sid = args.SID
    auth_token = args.auth_token
    client = Client(account_sid, auth_token)

    try:
    # Your PyTorch code here
        paeas
    except Exception as e:
        # Send a message with the error message
        message = client.messages.create(
            body=f"Your PyTorch code has crashed with the following error: {str(e)}",
            from_=from_number,
            to=to_number
        )




