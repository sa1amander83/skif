from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from rest_framework.generics import *

from apps.skif.models import SkierDay
from apps.skif_api.serializers import SkiSerializer


class SkierList(ListCreateAPIView):
    queryset = SkierDay.objects.all()
    serializer_class = SkiSerializer
class SkierDetail(RetrieveUpdateDestroyAPIView):
    pass