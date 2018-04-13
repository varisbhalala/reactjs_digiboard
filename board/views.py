from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from data import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import boardSerializer
import datetime
from register.permissions import IsAuthenticated,IsPublisher,IsAdvertiser
from rest_framework.decorators import api_view , permission_classes
def create_board(request):
	context={'state': models.States.objects.filter(country_id=101)}
	
	if request.POST:
		if 'delete' in request.POST:
			delete_board(request)
			file=None
			if 'list_board' in request.POST:
				file='../list_board'
			else:
				file='../get_board'
			return HttpResponseRedirect(file)
		else:
			board_id = request.POST['board_id']
			board = models.Board.objects.get(id=board_id)
			context={'board':board}
	return render(request,'create_board.html',context)

def save_board(request):
	if request.session:
		if 'update' in  request.POST:
			update(request)
		else:
			save(request)
	return HttpResponseRedirect("create_slot")

def save(request):
	lat = request.POST['lat']
	long_ = request.POST['lng']
	publisher_id = request.session['user_id']
	street = request.POST['street']
	area = request.POST['area']
	city = request.POST['city']
	state = models.States.objects.get(id= request.POST['state'])
	models.Board(lat=lat,lng=long_,street=street,area=area,city=city,state=state.name,publisher_id=publisher_id).save()

def update(request):
    print("--- -- ----  -- --- -"+request.POST['id'])
    board = models.Board.objects.get(id=request.POST['id'])
    board.lat = request.POST['lat']
    board.lng = request.POST['lng']
    board.area = request.POST['area']
    board.street = request.POST['street']
    board.city = request.POST['city']
    board.state = request.POST['state']
    board.updated_at = datetime.datetime.now()
    board.save()

def delete_board(request):
	models.Board.objects.filter(id=request.POST['board_id']).delete()

def get_board(request):
	if request.session:
		board = models.Board.objects.filter(publisher_id =request.session['user_id'])
		context = {"board":board}
		return render(request,'get_board.html',context)
	else:
		print("Please Sign In. . .")

def list_board(request):
	if 'user_id' in request.session:
		board = models.Board.objects.filter(publisher_id=request.session['user_id'])
		context={'board':board}
		return render(request,'list_boards.html',context)
	else:
		print("Please Sign In. . .")
		return render(request,'list_boards.html')

def test_bootstrap(request):
	return render(request,'test_bootstrap.html')

def requests(request):
	print (request.GET['id'])
	rid = request.GET['id']
	req = models.Requestboard.objects.get(id=rid)
	context={
	'req':req
	}
	return render(request,'requests.html',context)

def accept_or_decline(request):
    rid = request.GET['rid']
    decision = request.GET["approve_status"]
    print (decision)
    req = models.Requestboard.objects.get(id=rid)
    if decision == '1':
        print ("acceptttt")
        req.approve_status = 1
        req.save()
    elif decision == '2':
    	req.approve_status = 2
    	req.save()
    return render(request,'accept_or_decline.html')


@api_view(['GET' , 'POST'])
def create_board_api(request):
	if request.method == 'POST':
		serializer = boardSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'result':'board added'} , status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'POST'])
def get_board_api(request):
	print("data=======" , request.data)
	if request.method == 'POST':
		publisher_id = request.POST['publisher_id']
		board = models.Board.objects.filter(publisher = publisher_id)
		serializer = boardSerializer(board,many = True)
		return Response(serializer.data)

@api_view(['GET' ,'POST'])
def search_board_api(request):
	if request.method == "POST":
		boards = models.Board.objects.filter(city = request.POST['city'] , state = request.POST['state'])
		serializer = boardSerializer(boards , many = True)
		return Response(serializer.data)