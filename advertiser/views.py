
from django.shortcuts import render
from data import models
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render,HttpResponseRedirect
from data import models
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers.json import DjangoJSONEncoder
import json
from datetime import datetime, timedelta
import stripe
from rest_framework.response import Response
from rest_framework import status
from .serializers import paymentSerializer
from rest_framework.decorators import api_view

def advertiser(request):
	return render(request,'advertiser.html')

def search(request):
    context={}

    if request.POST:
        raise Http404("URL not exists")
    else:

        place = request.GET['search']

        place_name = request.GET['search_name']

        record = None
        if place == 'area':
            record = models.Board.objects.filter(area__contains=place_name)
            context={'record_area':record}
            return  render(request,'get_search.html',context)
            # return render(request, 'advertiser_panel.html' ,{'record':record})
        elif place == 'city':
            record = models.Board.objects.filter(city__contains=place_name)
            context={'record_city':record}
            return  render(request,'get_search.html',context)
            # return render(request, 'advertiser_panel.html' ,{'record':record})
        elif place == 'street':
            record = models.Board.objects.filter(street__contains=place_name)
            context={'record_street':record}
            return  render(request,'get_search.html',context)
            # return render(request, 'advertiser_panel.html' ,{'record':record})
        elif place == 'state':
            record = models.Board.objects.filter(state__contains=place_name)
            context={'record_state':record}
            return  render(request,'get_search.html',context)
            # return render(request, 'advertiser_panel.html' ,{'record':record})
    # context={'record':record}
    # return  render(request,'get_search.html',context)
            # return render(request, 'advertiser_panel.html' ,{'message':'no data is available'})

def search_done(request):
    if request.POST:
        raise Http404("URL not exists")
    else:
        place = request.GET['search']


        place_name = request.GET['search_name']
        if place == 'area':
            record = models.Board.objects.filter(area=place_name)
            return render(request, 'advertiser.html' ,{'record':record})
        elif place == 'city':
            record = models.Board.objects.filter(city=place_name)
            return render(request, 'advertiser.html' ,{'record':record})
        elif place == 'street':
            record = models.Board.objects.filter(street=place_name)
            return render(request, 'advertiser.html' ,{'record':record})
        elif place == 'state':
            record = models.Board.objects.filter(state=place_name)
            return render(request, 'advertiser.html' ,{'record':record})
        else:
            return render(request, 'advertiser.html' ,{'message':'no data is available'})
        place_name = request.GET['search_name']
        if place == 'area':
            record = models.Board.objects.filter(area=place_name)
        elif place == 'city':
            record = models.Board.objects.filter(city=place_name)
        elif place == 'street':
            record = models.Board.objects.filter(street=place_name)
        elif place == 'state':
            record = models.Board.objects.filter(state=place_name)
        else:
            return render(request, 'advertiser.html' ,{'message':'no data is available'})
        return render(request, 'advertiser.html' ,{'record':record})

def make_ad(request):
    state = models.States.objects.filter(country_id=101)
    context={'state': state}
    if request.POST:
        state = request.POST['state']
        city = request.POST['city']
        state = models.States.objects.get(id=state)
        print((state.name))

        board_obj = models.Board.objects.filter(city=city)
        state = models.States.objects.filter(country_id=101)
        context={'state':state,'board_obj':board_obj}
    return render(request,'make_ad.html',context)

def imp_master(request):
    return render(request,'impliment_master.html')


def plan(request):
    board = models.Board.objects.get(id = request.GET['board_id'])#right
    slot = models.Slot.objects.filter(board_id = request.GET['board_id'])#right
    # print("Board's ----------->>"+str(board.publisher_id))
    publisher = models.Publisher.objects.get(id = board.publisher_id)#right
    # print("Publisher's ----------->>"+str(publisher.id))
    return render(request, 'plan.html' , {'board': board , 'slot':slot, 'publisher':publisher})


def request_board(request):
    print ("hfjdhjfhdjfhdjfhjdfhdjfhjdhfjdhfjhdjfhjdhfjdhf" + request.POST['board_id'])
    print (request.POST['slot_id'])
    print ("userrrrrrrrrrrrrrrdvdfererererer"+"        "+str(request.session['user_id']))
    try:    
       status = models.Requestboard.objects.get(board_id = request.POST['board_id'] , slot_id = request.POST['slot_id'], advertiser_id = request.session['user_id'])
    except:
        request_board = models.Requestboard()
        # print(str("-------------->" + str(request.session['user_id'])))
        request_board.start_date=request.POST['start_date']
        request_board.advertiser_id = request.session['user_id']
        request_board.board_id = request.POST['board_id']
        request_board.publisher_id = request.POST['publisher_id']
        request_board.slot_id = request.POST['slot_id']
        request_board.request_status = 0
        request_board.approve_status = 0
        request_board.shown = 0
        request_board.save()
        
        request.session['publisher_id']=request.POST['publisher_id']
        #return HttpResponseRedirect('../make_ad/')
        return HttpResponseRedirect('../push_request/')

    else:
        print(str("-------------->"))
        return HttpResponseRedirect(request,'../plan/' , {'not_available' : "slot not available",})


def push_request(request):
    print ("PIUIYIYSBDJSBDNBS"+request.session["publisher_id"])
    return render(request,"push_request.html",{'publisher_id':request.session["publisher_id"]})


def advertiser_notify(request):
    aid = request.GET['advertiser_id']
    requests = models.Requestboard.objects.filter(advertiser_id=aid)
    context={
    'requests':requests,
    'aid':aid
    }
    return render(request,'advertiser_notify.html',context)

def upload_content(request):
    slot = models.Slot.objects.get(id = request.GET['slot_id'])
    board = models.Board.objects.get(id = request.GET['board_id'])
    request_board = models.Requestboard.objects.get(board_id = request.GET['board_id'],slot_id = request.GET['slot_id'],advertiser_id=request.session['user_id'])

    print("  --------------->  "+str(request_board.start_date + timedelta(days = 30)))

    context={'slot':slot, 'board_obj':board,'start_date':str(request_board.start_date),'end_date':str(request_board.start_date + timedelta(days = 30))}
    return render(request , "upload_content.html",context)

def submit_content(request):
    record = models.Payment.objects.filter(slot_id = request.POST['slot_id'])
    if record:
        return render(request, 'upload_content.html' , {'booked':'requested slot is already booked'})
    else:
        print("=====> "+ request.POST['start_date'])
        upload = models.Upload()
        upload.type = request.POST["content_type"]
        upload.location = request.FILES["content"]
        upload.current_state = 0
        upload.location = request.FILES['content']
        upload.seconds = request.POST['content_time']
        upload.advertiser_id = request.session["user_id"]
        upload.upload_date = datetime.now()
        upload.save()

        upload =  models.Upload.objects.filter(advertiser_id=request.session["user_id"]).order_by('-id')[0] #For Get Last entry of Upload inserted by current user(Advertiser)

        advertisement = models.Advertisement()
        advertisement.start_date = request.POST['start_date']
        advertisement.end_date = request.POST['end_date']
        advertisement.is_active=1
        advertisement.advertiser_id = request.session["user_id"]
        advertisement.board_id = request.POST['board_id']
        advertisement.slot_id = request.POST['slot_id']
        advertisement.upload_id = upload.id
        advertisement.save()
        return pay_charge(request)


def pay_charge(request):
    board_id = request.POST['board_id']
    slot_id = request.POST['slot_id']
    slot = models.Slot.objects.get(board_id = board_id , id = slot_id)
    print(str("board_id" + board_id))
    slot_price = slot.slot_price * 100
    print(str(slot_price))
    return render(request, 'pay_charge.html', {'slot' : slot_price, 'slot_tupple' : slot})


def pay(request):
    stripe.api_key = "sk_test_1h0vkCrOlyBJNHipBbdoV7h9"
    if request.method == "POST":
        slot_price = request.POST['slot_price']
        payment = models.Payment()
        payment.price = int(slot_price)
        payment.service_tax_ratio = 18
        payment.service_tax = (int(slot_price)) * 0.18
        payment.total_amount = int(slot_price) + ((int(slot_price)) * 0.18)
        token    = request.POST.get("stripeToken")
        payment.token = request.POST.get("stripeToken")
        payment.transaction_type = "card"
        payment.slot_id = request.POST['slot_id']
        payment.pay_log = "Paid"
        payment.advertiser_id = request.session['user_id']
        payment.publisher_id = request.POST['publisher_id']
        board_id = request.POST['board_id']
        slot_id = request.POST['slot_id']
        
        slot = models.Slot.objects.get(board_id = board_id , id = slot_id)
        print (str("Token===========> : " + token))
        # Charge the user's card:
        charge = stripe.Charge.create(
            amount= int(slot_price) * 100,
            currency="INR",
            description="Example charge",
            source=token,
        )
        payment.save()
        return HttpResponseRedirect("../welcome")

@api_view(['POST'])
def payment_api(request):
    print("data==================",request.data)
    if request.method == 'POST':
        serializer = paymentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print('data' , serializer)
            return Response({'result' : 'payment done'})
