from rest_framework import serializers
from .models import Rocket

class RocketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rocket
        fields = ('id', 'name', 'version', 'weight', 'dateProduced', 'dateLastLaunched')