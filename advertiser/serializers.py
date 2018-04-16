from rest_framework import serializers
from data import models

class paymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Payment
        fields = ('price' , 'total_amount' , 'token' , 'advertiser' , 'publisher' , 'slot')