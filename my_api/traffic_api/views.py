from django.shortcuts import render
from rest_framework import viewsets
from .models import Traffic
from .serializer import TrafficSerializer

class TrafficView(viewsets.ModelViewSet):
	queryset=Traffic.objects.all()
	serializer_class=TrafficSerializer
