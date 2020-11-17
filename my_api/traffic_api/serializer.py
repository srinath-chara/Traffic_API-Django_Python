from rest_framework import serializers
from .models import Traffic

class TrafficSerializer(serializers.ModelSerializer):
	class Meta:
		model=Traffic
		fields=('id','week','speed')