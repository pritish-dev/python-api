from twilio.rest import Client
import os


# Replace these with your Twilio account SID and auth token
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Replace this with your Twilio phone number
twilio_phone_number = 'xxxxxxxxxx'

# Replace this with the recipient's phone number in India
recipient_phone_number = 'xxxxxxxxxx'

def make_phone_call():
    try:
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            to=f'+91{recipient_phone_number}',  # Adding +91 for India country code
            from_=twilio_phone_number,
            url='http://localhost:5000/custom_message.xml',  # Update this with your hosted XML file URL
            method='GET'
        )

        print(f"Phone call initiated! Call SID: {call.sid}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    make_phone_call()
