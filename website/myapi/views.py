from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import RocketSerializer
from .models import Rocket

class RocketViewSet(viewsets.ModelViewSet):
    queryset = Rocket.objects.all().order_by('name')
    serializer_class = RocketSerializer