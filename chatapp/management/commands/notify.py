from django.core.management.base import BaseCommand
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Command(BaseCommand):
    # help = 'Send a message to the chat'
    help = 'Display current time'

    # def add_arguments(self, parser):
    #     parser.add_argument('message', type=str)

    def handle(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        print('working...')

        async_to_sync(channel_layer.group_send)("chat_test", {
            "type": "chat_message",
            "message": "notification",
        })

    # def handle(self, *args, **options):
    #     message = options['message']
    #     channel_layer = get_channel_layer()
    #     async_to_sync(channel_layer.group_send)(
    #         'chat',
    #         {
    #             'type': 'chat_message',
    #             'message': message,
    #             'time': timezone.now()
    #         }
    #     )