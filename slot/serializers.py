from rest_framework import serializers
from data import models

class slotSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Slot
        fields = ('__all__')