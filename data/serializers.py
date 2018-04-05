from rest_framework import serializers 
from . import models

class stateSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.States
		fields = ('__all__')

class citySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Cities
		fields = ('__all__')