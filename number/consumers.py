from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from number.models import Number
from number.serializers import NumberSerializer

'''class FooConsumer(AsyncWebsocketConsumer):
    async def websocket_connect(self, event):
        user = self.scope["user"]
        await self.accept()'''


class PrizeConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'prizes'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data_json = json.loads(text_data)
        text = data_json['text']
        user = data_json['user']
        print('10000000')
        '''club_message = ClubMessage.objects.create(user_id=user, text=text)
        serializer = ClubMessageSerializer(club_message)
        message_serialized = serializer.data
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'have_prize',
                'message_serialized': message_serialized
            }
        )'''

    def have_prize(self, event):
        message_serialized = event['message_serialized']
        print('message club: ', message_serialized)
        self.send(text_data=json.dumps(
            message_serialized
        ))
