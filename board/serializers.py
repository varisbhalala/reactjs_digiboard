from rest_framework import serializers
from data import models


class boardSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Board
		fields = ('__all__')

class create_boardSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Board
		fields = ('__all__')