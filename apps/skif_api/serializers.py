
from rest_framework import serializers

from apps.skif.models import SkierDay


class SkiSerializer(serializers.ModelSerializer):
    class Meta:
        model= SkierDay
        fields = ('id', 'runner', 'day_select', 'day_distance', 'day_time', 'day_average_temp','photo')