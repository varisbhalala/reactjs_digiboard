import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from data.models import Requestboard
from django.core import serializers
import pdb


#@channel_session_user_from_http
def ws_connect(message):
    print (message['path'])
    requests=Requestboard.objects.all()
    res=serializers.serialize("json",requests)
    Group('users').add(message.reply_channel)
    Group('users').send({
        'text': json.dumps({
            'accept': True
        })
    })


@channel_session_user
def ws_disconnect(message):
    Group('users').send({
        'text': json.dumps({
            'username': message.user.username,
            'is_logged_in': False
        })
    })
    Group('users').discard(message.reply_channel)

@channel_session_user
def ws_receive(message):
    data=json.loads(message.content.get('text'))
    if (data.get('decision') != None):
        dec = data.get('decision')
        ad = data.get('advertiser')
        Group('users').send({
            'text':json.dumps({
                'decision': dec,
                'advertiser':ad
                })
            })
    if (data.get('coin') != None):
        print ("data.    "+str(data.get('coin')))
        pid=data.get('coin')
        Group('users').send({
        'text':json.dumps({
            'pid':pid
            })
        })

    