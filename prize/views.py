from rest_framework.generics import ListAPIView, UpdateAPIView
from prize.serializers import PrizeSerializer
from number.models import Number
from rest_framework.permissions import IsAuthenticated
from lottee.permissions import ReadOnly


class PrizeListView(ListAPIView):
    permission_classes = [IsAuthenticated | ReadOnly]
    serializer_class = PrizeSerializer

    def get_queryset(self):
        user = self.request.user
        prizes = Number.objects.filter(user_id=user, won=True)
        return prizes


class PrizeUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Number.objects.all()
    serializer_class = PrizeSerializer

    '''def partial_update(self, request, *args, **kwargs):
        serializer = UserSerializer(
            instance=request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )'''
