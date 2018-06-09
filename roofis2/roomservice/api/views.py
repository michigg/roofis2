from __future__ import unicode_literals

from roomservice.models import Booking
from roomservice.api.serializers import BookingSerializer

from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


@permission_classes((AllowAny,))
class ApiBooking(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        roomId = self.request.query_params.get('room_id')

        if roomId:
            queryset = queryset.filter(room=roomId)
        return queryset
