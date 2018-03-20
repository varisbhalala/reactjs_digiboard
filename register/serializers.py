from rest_framework import serializers
from data import models

class userSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.User
		fields = ('username','email')

