import os
from twilio.rest import Client


auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
verify_sid = os.environ.get('TWILIO_VERIFY_SID')

class MessageHandler:
    phone_number = None

    def __init__(self, phone=None):
        self.phone_number = phone

    def send_otp_via_message(self):
        client = Client(account_sid, auth_token)
        verification = client.verify.v2.services(verify_sid).verifications.create(to=self.phone_number, channel="sms")
        print(verification.status)

    def verify_message_otp(self, otp):
        client = Client(account_sid, auth_token)
        verification_check = client.verify.v2.services(verify_sid).verification_checks.create(to=self.phone_number, code=otp)
        return verification_check.status
