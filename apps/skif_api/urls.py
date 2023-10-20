
from django.contrib import admin
from django.urls import path, include
from .views import SkierList, SkierDetail
urlpatterns = [
    path('<int_pk>/',SkierDetail.as_view(), name='detail'),
    path('',SkierList.as_view(), name='list'),


]
