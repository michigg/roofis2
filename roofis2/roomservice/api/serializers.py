from roomservice.models import Booking, Room
from rest_framework import serializers


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id',)


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    room = RoomSerializer(many=False, read_only=True)
    start_date = serializers.DateField(format='iso-8601')
    end_date = serializers.DateField(format='iso-8601')
    start_time = serializers.TimeField(format='iso-8601')
    end_time = serializers.TimeField(format='iso-8601')

    class Meta:
        model = Booking
        fields = ('id', 'room', 'start_date', 'end_date', 'start_time', 'end_time')
