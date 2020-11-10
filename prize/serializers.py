from rest_framework import serializers
from lot.serializers import LotPrizeSerializer
from number.models import Number


class PrizeSerializer(serializers.ModelSerializer):
    lot = LotPrizeSerializer(read_only=True)

    class Meta:
        model = Number
        fields = ['id', 'lot', 'num', 'score']
        read_only_fields = ('id', 'lot', 'num')
