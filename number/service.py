import requests
from rest_framework.utils import json
from number.models import Number
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from number.serializers import WinnerSerializer


def choose_winners(lot):
    data_ = [1]
    if lot.players > 1:
        url = 'https://api.random.org/json-rpc/2/invoke'
        json_ = {
            "jsonrpc": "2.0",
            "method": "generateIntegers",
            "params": {
                "apiKey": "fc702e8a-53f0-4dc1-83f2-63c07fb0e835",
                "n": lot.winners,
                "min": 1,
                "max": lot.players,
                "replacement": False
            },
            "id": lot.id
        }
        r = requests.post(url, json=json_)
        json_ = json.loads(r.text)
        print(json_)
        print(json_['result']['random']['completionTime'])
        lot.winners_complete = json_['result']['random']['completionTime']
        data_ = json_['result']['random']['data']

    winners = Number.objects.filter(lot=lot, num__in=data_)  # .update(won=True)
    lot.active = False
    lot.save()

    winners_serializer = WinnerSerializer(winners, many=True)
    w = winners.update(won=True)

    print('winners count %s' % w)
    # websocket
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('prize', {
        'type': 'have_prize',
        'info': {
            'lot_id': lot.id,
            'lot_name': lot.title,
            'winners': winners_serializer.data
        }
    })
