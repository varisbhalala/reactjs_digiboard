# from rest_framework import serializers 
from data import models
from rest_framework_json_api import serializers

class userSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = models.User
		fields = ('__all__')
		

class confirmMailSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.User
		fields = ('__all__')

class publisherSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Publisher
		fields = ('__all__')

class advertiserSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Advertiser
		fields = ('__all__')

