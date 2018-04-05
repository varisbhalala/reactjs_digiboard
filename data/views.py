from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . serializers import stateSerializer , citySerializer
@api_view(['GET' , 'POST'])
def state_api(request):
    if request.method == 'GET':
        state = models.States.objects.filter(country_id = 101)
        serializer = stateSerializer(state,many=True)
        return Response(serializer.data)

@api_view(['GET' , 'POST'])
def city_api(request):
    if request.method == 'GET':
        state_index = request.GET['state_index']
        city = models.Cities.objects.filter(state_id = state_index)
        serializer = citySerializer(city, many=True)
        return Response(serializer.data)