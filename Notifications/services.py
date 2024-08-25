# from celery import shared_task
# from twilio.rest import Client
# @shared_task(bind=True)
# def my_task(self):
#     for i in range(10):
#         print(i)
#     return "Done"

from twilio.rest import Client
from django.conf import settings
from main import settings
import json

class TwilioClient:
    def __init__(self):
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def send_whatsapp_message(self, to, body, buttons=None):
        message_data = {
            'content_sid':'HX8472c88688bb676a1f29b1d31f7d82ee',
            'from_': f'whatsapp:+{settings.TWILIO_WHATSAPP_NUMBER}',
            'body': body,
            'to': f'whatsapp:+{to}',
            'content_variables': json.dumps({"1": "Name"})
        }
        
        # if buttons:
        #     message_data['persistent_action'] = ['reply']
        #     message_data['interactive'] = {
        #         'type': 'button',
        #         'action': {
        #             'buttons': buttons
        #         }
        #     }

        message = self.client.messages.create(**message_data)
        return message.sid

    def send_buttons_example(self, to):
        buttons = [
            {'type': 'reply', 'reply': {'id': 'update_info', 'title': 'Update Info'}},
            {'type': 'reply', 'reply': {'id': 'rsvp', 'title': 'RSVP'}}
        ]
        return self.send_whatsapp_message(to, 'Choose an option:')
