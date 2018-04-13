from django.shortcuts import render, HttpResponseRedirect
from data import models
import json
from rest_framework.response import Response
from django.db import models as mod
from django.http import JsonResponse
from datetime import datetime
from rest_framework import status
from .serializers import slotSerializer
from rest_framework.decorators import api_view
# ================ I Have to Check The Role of the user =================

def create_slot(request):
	context={'board_id' : models.Board.objects.filter(publisher_id = request.session['user_id'])}
	board_obj = models.Board.objects.filter(publisher_id = request.session['user_id'])
	print("------->"+str(board_obj))
	if request.POST:
		from_ = request.POST['from']
		to = request.POST['to']
		total=int(request.POST['diff'])
		board_id = int(request.POST['all_board'])

		if total==15 or total == 30 or total == 45:
			total = total * 60
		else:
			total = total * (60*60)

		price = request.POST['price']
		user_id = request.session['user_id']
		print("User ID ===========> " + str(user_id))
		Slot = models.Slot()
		Slot.from_field = from_
		Slot.to = to
		Slot.board_id = board_id
		Slot.total = total
		Slot.slot_price = price
		Slot.publisher_id = user_id
		print(from_+" "+to+" ----------> Pub =.  "+str(user_id))
		Slot.save()

		print(str("selected" + request.POST['all_board']))
		context={
			'board_id' : models.Board.objects.filter(publisher_id = request.session['user_id']),
			'selected':board_id
		}
		return HttpResponseRedirect("../create_slot/?board="+str(board_id))
	return render(request,'create_slot.html',context)

# def list_slot(request):
# 	slot  = models.Slot.objects.filter(publisher_id = request.session['user_id'])
# 	context={'slot':slot}
# 	if 'remove' in request.POST:
# 		delete(request)
# 		return HttpResponseRedirect("../list_slot")
# 	return render(request,'list_slot.html',context)

def delete(request):
	models.Slot.objects.get(id=request.POST['id']).delete()

def listSlot(request):

	request_board_id = request.GET['board_id'].strip()
	slots = models.Slot.objects.filter(board_id = request_board_id)
	context = {
		'slot' : slots
	}
	return render(request , 'get_slot.html',context)




def check_slot(request):
	from_ = request.GET['from']+":00"#.000000"

	from_c =  datetime.strptime(from_, "%H:%M:%S%f").time()
	# mod.TimeField(from_)
	board_id = request.GET['board_id']
	response_data = {}
	
	slots = models.Slot.objects.filter(board_id = board_id)
	
	for i in slots:
		if from_c >= i.from_field and from_c <= i.to:
			#print(str(i.from_field+"IKYiuo;l+++++++"+ i.to))
			response_data['is_success'] = True
			break
		else :
			print("Else part --------->"+str(i.from_field)+"IKYiuo;l+++++++"+ str(i.to))
			response_data['is_success'] = False		
	return JsonResponse(response_data)
	




def deleteSlot(request):
	data = models.Slot.objects.get(id = request.POST['slot_id'])
	data.delete()
	return HttpResponseRedirect("../create_slot")


@api_view(['POST'])
def create_slot_api(request):
	if request.method == 'POST':
		serializer = slotSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"result" : "slot created"},status = status.HTTP_201_CREATED)
		return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)