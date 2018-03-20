from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def mail(request):
    send_mail('Mail_from_mayur', 'Successfully sent mail from django', 'mayurchhapra@gmail.com', ['mayurchhapra@gmail.com'])
    return render(request,'mail.html')
