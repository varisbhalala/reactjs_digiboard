from rest_framework import permissions
import jwt
from data import models
from django.http import JsonResponse ,HttpResponse
from rest_framework.response import Response
from rest_framework import status , generics
from rest_framework.exceptions import APIException


class IsAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def _get_token(request=None):
        return request.META.get('HTTP_AUTHORIZATION') or request.GET.get('token')

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        token = request.META.get('HTTP_AUTHORIZATION')
        token_b = token.encode("utf-8")
        # print ("tokennnn",token)
        try: 
            print("inside is authenticated   =============>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            payload = jwt.decode(token, 'digi')
            print ("usernammmmmmme",payload.get('data')['username'],"PAsss:::",payload.get('data')['password'])
            user = models.User.objects.get(username = payload.get('data')['username'] , password = payload.get('data')['password'])
            print("user data==============>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" , user.role)
            if user:
                request.user = user
                return True
            else:
                return False
        
        except jwt.ExpiredSignature as e:
            raise jwt.ExpiredSignature("Signature Expired")

        except (jwt.ExpiredSignature, jwt.DecodeError, jwt.InvalidTokenError) as e:
            print ("usernammmmmmme  ",e)
            return False   
     
class IsPublisher(permissions.BasePermission):
    
    def _get_token(request=None):
        return request.META.get('HTTP_AUTHORIZATION') or request.GET.get('token')

    def has_permission(self,request,view):
        print("inside is publisher   =============>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        token = request.META.get('HTTP_AUTHORIZATION')
        token_b = token.encode("utf-8")
        try:
            payload = jwt.decode(token, 'digi')
            # print ("usernammmmmmme",payload.get('usename'))
            user = models.User.objects.get(username = payload.get('data')['username'] , password = payload.get('data')['password'])
            # print("user data==============>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" , user.role)
            if user.role == 'p':
                request.user = user
                return True
            else:
                return False

        except (jwt.ExpiredSignature, jwt.DecodeError, jwt.InvalidTokenError) as e:
            print ("usernammmmmmme",e)
            return False

class IsAdvertiser(permissions.BasePermission):

    def _get_token(request=None):
        return request.META.get('HTTP_AUTHORIZATION') or request.GET.get('token')

    def has_permission(self,request,view):
        print("inside is advertiser   =============>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        token = request.META.get('HTTP_AUTHORIZATION')
        token_b = token.encode("utf-8")
        try:
            payload = jwt.decode(token, 'digi')
            print ("usernammmmmmme==================Advertise",payload)
            print ("usernammmmmmme==================Advertise",payload.get('usename'))
            user = models.User.objects.get(username = payload.get('data')['username'] , password = payload.get('data')['password'])
            # print("user data==============>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" , user.role)
            if user.role == 'a':
                request.user = user
                return True
            else:
                return False

        except (jwt.ExpiredSignature, jwt.DecodeError, jwt.InvalidTokenError) as e:
            print ("usernammmmmmme",e)
            return False