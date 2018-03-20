from django.shortcuts import render, HttpResponseRedirect
import datetime
from data.models import Publisher , Advertiser , User, States, Cities
from data import models
from django.utils.crypto import get_random_string
from django.core.mail import send_mail , EmailMessage
from django.http import HttpResponse, Http404, HttpResponse
import logging
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from MySQLdb import *



#Navigation
def navigation(request):
    return render(request,'navigation.html')

#Registration_form
def register(request):
    state = States.objects.filter(country_id=101)
    print(state)
    context={
        'state': state,
    }

    if request.POST:
        role = request.POST.get('role')
        if role == 'p':
            form1 = Publisher()
        elif role == 'a':
            form1 = Advertiser()

        state = States.objects.get(id=request.POST.get('state') )    #Get the state form DB


        form1.name = request.POST.get('name')
        form1.contact = request.POST.get('contact_number')
        form1.email = request.POST.get('email')
        form1.avatar = request.FILES['image']
        form1.company_name = request.POST.get('company_name')
        form1.company_address = request.POST.get('company_address')
        form1.state = state.name
        form1.city = request.POST.get('city')
        created_at = datetime.datetime.now()

        form1.save()

        if role == 'p':
            record = Publisher.objects.all().order_by('-id')[0]
        elif role == 'a':
            record = Advertiser.objects.all().order_by('-id')[0]

        form_user = User()
        form_user.username = request.POST.get('username' )
        form_user.password = request.POST.get('password')
        created_at = datetime.datetime.now()
        form_user.role = request.POST.get('role')
        form_user.uid = form1.id
        form_user.save()
        return HttpResponseRedirect('/login/') # Red

    return render(request,'register.html',context)
#It Shows map
def create_board(request):
    context={}
    if request.POST:
            board_id = request.POST['map']
            board = models.Board.objects.get(id=board_id)
            context={'board':board}
    return render(request,'create_board.html',context)

#Save Board
def save_board(request):
    if request.session:
        if 'update' in  request.POST:
            update(request)
        else:
            save(request)
    return render(request,'create_board.Html')

def save(request):
    lat = request.POST['lat']
    long_ = request.POST['lng']
    publisher_id = request.session['id']
    street = request.POST['street']
    area = request.POST['area']
    city = request.POST['city']
    state = request.POST['state']
    board = models.Board(lat=lat,lng=long_,street=street,area=area,city=city,state=state,publisher_id=publisher_id)
    board.save()

def update(request):
    print("--- -- ----  -- - -"+request.POST['id'])
    board = models.Board.objects.get(id=request.POST['id'])
    board.lat = request.POST['lat']
    board.lng = request.POST['lng']
    board.area = request.POST['area']
    board.street = request.POST['street']
    board.city = request.POST['city']
    board.state = request.POST['state']
    board.updated_at = datetime.datetime.now()
    board.save()


def get_board(request):
    if request.session:
        board = models.Board.objects.filter(publisher_id =request.session['id'])
        context = {"board":board}

        return render(request,'getboard.html',context)

#For Fetch Ajax Data(State-City)
def ajaxData(request):
    #request.GET['state_id']
    city = Cities.objects.filter(state_id = request.GET['state_id'])
    context={
    'city':city
    }
    return render(request,'ajaxData.html',context)


#Display the Forgot Password Page
def forgot_password(request):
    return render(request, 'forgot_password.html')

#Check the mail of the user entered.
def check_email(request):
    if request.POST:
        role = request.POST.get('role')

        if role == 'p':
            record = Publisher.objects.get(email=request.POST.get('email'))

        elif role == 'a':
            record = Advertiser.objects.get(email=request.POST.get('email'))

        if record:
            unique_token = get_random_string(length=32)
            record1 = User.objects.get(uid=record.id,role=role)
            record1.token = unique_token
            record1.save()
            send_mail('Mail_from_mayur', "127.0.0.1:8000/new_password/?key="+unique_token,'digiboard2030@gmail.com', [request.POST.get('email')])
            # email = EmailMessage('reset password', 'your key is here' , request.POST.get('email'))
            # email.send()
            return HttpResponseRedirect('/forgot_password/')

        else:
            return render(request, 'forgot_password.html',{'incorrect_email': "Email_id is incorrect"})

#From mail link, It will be redirected here.
def new_password(request):
    token1 = request.GET['key']
    print(token1)
    record1 = User.objects.filter(token=token1)
    return render(request, 'new_password.html',{'record1': record1})

#For Store new Password
def save_password(request):
    user = User.objects.get(id = request.POST.get('user_id'))
    new_password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    if new_password == confirm_password:
        user.password = new_password
        user.token = "NULL"
        user.updated_at = datetime.datetime.now()
        user.save()
        return HttpResponseRedirect('/login/')
    else:
        return render(request, 'new_password.html',{'incorrect_email': "new password and confirm password does not match"})

#Get Login page
def login(request):
    context={}
    if request.POST:

        username_session = request.POST.get('username')
        password_session = request.POST.get('password')
        record = None
        try:
            record = User.objects.get(username = username_session, password = password_session)
        except User.DoesNotExist:
            record = None
        print(record)
        if record:
            #request.session['username'] = username_session
            if record.role == 'p':
                record1 = Publisher.objects.filter(id = record.uid)
                request.session['name'] = record1[0].name
                request.session['id'] = record1[0].id
                return render(request,'publisher_panel.html',{'record1':record1})
            elif record.role == 'a':
                record1 = Advertiser.objects.filter(id = record.uid)
                return render(request,'advertiser_panel.html',{'record1':record1})
        else:
            context={'invalid':'Missmatch Username and Password'}
    return render(request, 'login.html',context)

#Delete session
def logout(request):
    del request.session['name']
    del request.session['id']
    return HttpResponseRedirect('/navigation/')



#----------------------------- R & D -----------------------------

def check_user(request):

    if request.method == "POST":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        login = request.GET["login"].strip()
        user = None
        try:
            try:
                user = User.objects.get(username = login)
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."
    return JsonResponse(response_data)

def check_email_reg(request):

    if request.method == "POST":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        email = request.GET["email"].strip()
        role = request.GET["role"].strip()
        user = None

        try:
            try:
                if role=='a':
                    user = Advertiser.objects.get(email=email)
                else:
                    user = Publisher.objects.get(email=email)
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."
    return JsonResponse(response_data)

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
            return render(request, 'advertiser_panel.html' ,{'record':record})
        elif place == 'city':
            record = models.Board.objects.filter(city=place_name)
            return render(request, 'advertiser_panel.html' ,{'record':record})
        elif place == 'street':
            record = models.Board.objects.filter(street=place_name)
            return render(request, 'advertiser_panel.html' ,{'record':record})
        elif place == 'state':
            record = models.Board.objects.filter(state=place_name)
            return render(request, 'advertiser_panel.html' ,{'record':record})
        else:
            return render(request, 'advertiser_panel.html' ,{'message':'no data is available'})




def slot(request):
    return render(request, 'slot.html')


def save_slot(request):
    form = models.Slot()
    form.from_field = datetime.datetime.strptime(request.POST['from'] , '%H:%M')
    form.to = datetime.datetime.strptime(request.POST['to'] , '%H:%M')
    a = str(datetime.datetime.strptime(request.POST['to'] , '%H:%M') - datetime.datetime.strptime(request.POST['from'] , '%H:%M'))
    h = a.split(":")
    form.total = int(h[0])*60*60 + int(h[1])*60 + int(h[2])
    #
    # form.to = request.POST['to']
    # print( request.POST['to'])
    # form.total = request.POST['total']
    form.slot_price = request.POST['price']
    form.publisher_id = request.session['id']
    form.save()
    return HttpResponseRedirect('/login/')
