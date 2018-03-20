from django import template
from data import models

register = template.Library()

@register.simple_tag
def get_slot(sid):
	slot = models.Slot.objects.get(id=sid)
	fromtime = str(slot.from_field)
	totime = str(slot.to)
	return ("%s to %s" % (fromtime,totime)) 

@register.simple_tag
def check_for_new(pid,role):
	if (role == 'p'):
		requests = models.Requestboard.objects.filter(publisher_id=pid,shown=0)
		if requests:
			return 1
		else:
			return 0
	elif (role == 'a'):
		requests = models.Requestboard.objects.filter(advertiser_id=pid,request_status=0,approve_status=1 or 2)
		print (requests)
		if requests:
			print ("advertiser heere")
			return 2
		else: 
			return 0


@register.simple_tag
def update_req(pid,role):
    if (role == 'p'):
        requests = models.Requestboard.objects.filter(publisher_id=pid,shown=0)
        for r in requests:
            r.shown=1
            r.save()

    elif (role == 'a'):
        requests = models.Requestboard.objects.filter(advertiser_id=pid,request_status=0,approve_status=1 or 2)
        for r in requests:
            r.request_status = 1
            r.save()
    return " "
