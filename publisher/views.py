from django.shortcuts import render
from data import models

def publisher(request):
	#requests=models.Requestboard.objects.filter(publisher_id=request.GET["publisher_id"])
    
    pid = request.GET["publisher_id"]
    requests = models.Requestboard.objects.filter(publisher_id=pid)
    context = {
    'requests':requests,
    'pid':pid
    }
    return render(request,'publisher.html',context)