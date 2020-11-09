from rest_framework import serializers
from lot.serializers import LotPrizeSerializer
from number.models import Number


class PrizeSerializer(serializers.ModelSerializer):
    lot = LotPrizeSerializer()

    class Meta:
        model = Number
        fields = ['id', 'lot', 'num']
