import random
from rest_framework.generics import UpdateAPIView
from number.serializers import NumberSerializer
from number.models import Number
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from lottee.permissions import ReadOnly
from number.service import choose_winners
from django.db import connection


class NumberUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]

    def partial_update(self, request, *args, **kwargs):
        numbers = Number.objects.select_related('lot__user').filter(lot_id=self.request.data['lot_id'])
        # print(numbers)
        lot_user_numbers = numbers.filter(user_id=request.user.id)
        if not len(lot_user_numbers):
            print('USER NO HAVE NUMBER')
            lot_numbers_free = numbers.filter(user_id=None)
            print(lot_numbers_free)
            if lot_numbers_free:
                print('HAVE FREE')
                random_idx = random.randint(0, len(lot_numbers_free) - 1)
                lot_number = lot_numbers_free[random_idx]
                if request.user.energy >= lot_number.lot.energy and request.user != lot_number.lot.user:
                    print('HAVE ENERGY AND NOT YOUR LOT')
                    request.user.energy -= lot_number.lot.energy
                    request.user.save(update_fields=['energy'])
                    lot_number.user = request.user
                    lot_number.save(update_fields=['user'])
                    if len(lot_numbers_free) <= 1 and lot_number.lot.active:
                        choose_winners(lot_number.lot)

                    print('RESPONSE 2000 ', lot_number)
                    return Response(
                        status=status.HTTP_200_OK,
                        data={'number': lot_number.num, 'active': lot_number.lot.active}
                    )
        # serializer = NumberSerializer(numbers, many=True)
        # print('Total requests count: %s' % len(connection.queries))
        # data=serializer.data,
        return Response(status=status.HTTP_403_FORBIDDEN)

    '''def patch(request, pk):
        
        
        
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
            return Response(status=status.HTTP_403_FORBIDDEN)
        
            return Response(
                data={'No have energy' if lot_number.lot.energy > request.user.energy else 'You\'r lot'},
                status=status.HTTP_424_FAILED_DEPENDENCY
                if lot_number.lot.energy > request.user.energy
                else status.HTTP_428_PRECONDITION_REQUIRED
            )
        
        serializer = NumberSerializer(lot_number)
        print('Total requests count: %s' % len(connection.queries))
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
'''