import random
from rest_framework.views import APIView
from number.serializers import NumberSerializer
from number.models import Number
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lottee.permissions import ReadOnly
from number.service import choose_winners
from django.db import connection


class NumberListUpdateView(APIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    @staticmethod
    def post(request, pk):
        numbers = Number.objects.select_related('lot__user').filter(lot_id=pk)
        lot_user_numbers = numbers.filter(user_id=request.user.id)
        if len(lot_user_numbers):
            return Response(status=status.HTTP_226_IM_USED)
        lot_numbers_free = numbers.filter(user_id=None)
        if not lot_numbers_free:
            return Response(status=status.HTTP_204_NO_CONTENT)
        random_idx = random.randint(0, len(lot_numbers_free) - 1)
        lot_number = lot_numbers_free[random_idx]
        if lot_number.lot.energy > request.user.energy or lot_number.lot.user == request.user:
            return Response(
                data={'No have energy' if lot_number.lot.energy > request.user.energy else 'You\'r lot'},
                status=status.HTTP_424_FAILED_DEPENDENCY
                if lot_number.lot.energy > request.user.energy
                else status.HTTP_428_PRECONDITION_REQUIRED
            )
        request.user.energy -= lot_number.lot.energy
        request.user.save(update_fields=['energy'])
        lot_number.user = request.user
        lot_number.save(update_fields=['user'])
        if len(lot_numbers_free) <= 1 and lot_number.lot.active:
            choose_winners(lot_number.lot)
        serializer = NumberSerializer(lot_number)
        print('Total requests count: %s' % len(connection.queries))
        return Response(serializer.data)
