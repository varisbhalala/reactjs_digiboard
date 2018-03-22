from django.shortcuts import render, HttpResponseRedirect ,get_object_or_404
from data import models
from django.core.mail import send_mail
from django.utils.crypto import get_random_string #For generate Random Tokens
from django.core.exceptions import ObjectDoesNotExist #For Exception
import sys
import json
from django.http import JsonResponse ,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import userSerializer
from digiboard_project import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
def first_step_reg(request):
	
	context={}
	if request.POST:
		unique_token = get_random_string(length=32)
		user = models.User(username=request.POST['username'],password=request.POST['password'],token=unique_token,email=request.POST['email'],role=request.POST['role'])
		user.save()
		send_mail('Confirm Your Mail', sys.argv[-1]+"/confirmMail/?key="+unique_token,'digiboard2030@gmail.com', [request.POST['email']])
		context={'data':'-x-x-'}

	return render(request,"first_step_registrationtest.html",context)

def confirmMail(request):
	context={}
	if request.GET:
		key = request.GET['key']
		user = models.User.objects.get(token=key)
		if user:
			request.session['username'] = user.username
			request.session['role'] = user.role
			request.session['user_id'] = user.id
			#print(" User_Id on Session ============= "+str(request.sessionp['user_id']))
			context={'email':'email'}
	return render(request,'confirm_Mail.html',context)

def ajaxData(request):
	city = models.Cities.objects.filter(state_id = request.GET['state_id'])
	context={
	'city':city
	}
	return render(request,'ajaxData.html',context)

def profile(request):
	print(request.session['user_id'])
	user=None
	state = models.States.objects.filter(country_id=101)
	context={
        'state': state,
    }
	if request.POST:
		if request.session['role'] == 'p':
			user = models.Publisher()
		else:
			
			user = models.Advertiser()

		state = models.States.objects.get(id=request.POST.get('state') )    #Get the state form DB


		print("Name =  "+str(request.POST['name'])+" Contact = "+str(request.POST['contact'])+" Avatar "+str(request.FILES['avatar'])+" Com_name= "+str(request.POST['cname']) +" Com_Add= "+ str(request.POST['address'])+" State = "+ str(state.name)+" City= "+str(request.POST['city']) +" User_id_FK= "+str(request.session['user_id']))
		#For Save data to Advertiser/Publisher tbl....
		user.name= request.POST['name']
		user.contact = request.POST['contact']
		user.avatar = request.FILES['avatar']
		user.company_name = request.POST['cname']
		user.company_address = request.POST['address']
		user.city = request.POST['city']
		user.state=state.name
		user.user_id = request.session['user_id']
		user.save()
		request.session['name'] = request.POST['name']
		#For Remove Token value....
		user = models.User.objects.get(username=request.session['username'])
		user.token=None
		user.save()
		return HttpResponseRedirect('../welcome')
	return render(request,"profile.html",context)

def welcome(request):
    print ("heyyyyyyyyyyyyyyyyyyyyyyy"+str(request.session['user_id']))
    role=request.session['role']
    if role=='p':
        publisher_id=request.session['user_id']
        try:
            requests=models.Requestboard.objects.filter(publisher_id=publisher_id)
        except:
        	requests=None
    return render(request,'welcome.html')

#Get Login page
def login(request):
    print ("hereeee")
    context={}
    if request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        record = None
        try:
            user_login_row = models.User.objects.get(username = username, password = password)
        except models.User.DoesNotExist:
            user_login_row = None
        print(user_login_row)
        if user_login_row:
            #request.session['username'] = username_session
            if user_login_row.role == 'p':
                user_role_id = models.Publisher.objects.get(user_id= user_login_row.id)
                request.session['user_id'] = user_role_id.id
                request.session['name'] = user_role_id.name
                request.session['role'] = user_login_row.role
                return HttpResponseRedirect('../welcome')
            elif user_login_row.role == 'a':
            	user_role_id = models.Advertiser.objects.get(user_id = user_login_row.id)
            	request.session['user_id'] = user_role_id.id
            	request.session['name'] = user_role_id.name
            	request.session['role'] = user_login_row.role
            	return HttpResponseRedirect('../welcome')
        else:
            context={'invalid':'Missmatch Username and Password'}
    print ("hereeeesfasdfadsfasdfasdfw")
    return render(request, 'login.html',context)

def logout(request):
	if 'username' in request.session:
		del request.session['username']
	if 'role' in request.session:
		del	request.session['role']
	if 'user_id' in request.session:
		del	request.session['user_id']
	if 'name' in request.session:
		del	request.session['name']
	if 'publisher_id' in request.session:
		del request.session['publisher_id']
	return HttpResponseRedirect('../login')





def check_user(request):

    if request.method == "POST":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        login = request.GET["login"].strip()
        user = None
        try:
            try:
                user = models.User.objects.get(username = login)
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

def check_email(request):

    if request.method == "POST":
        raise Http404("URL doesn't exists")
    else:
        response_data = {}
        email = request.GET["email"].strip()
        
        user = None

        try:
            try:
              
                user = models.User.objects.get(email=email)
                
                    
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


@api_view(['GET' , 'POST'])
def userList(request):
    if request.method == 'GET':    
        user1 = models.User.objects.all()
        serializer = userSerializer(user1, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = json.dumps(serializer.data)
            content1 = json.loads(content)
            token = content1["token"]
            email = content1["email"]
            send_mail('Confirm Your Mail',"http://" +sys.argv[-1]+"/confirmMail/?key="+token,'digiboard2030@gmail.com', [email])
            # token = content['token']
            # print("token======> " )
            return Response({'result':'user_added'} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
