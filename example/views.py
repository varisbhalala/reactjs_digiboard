from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm



def user_list(request):
    return render(request, 'example/user_list.html',{'id':1})

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect('../')
        else:
            print(form.errors)
    return render(request, 'example/log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('../log_in/')

def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        print (form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../log_in/')
        else:
            print(form.errors)
    return render(request, 'example/sign_up.html', {'form': form})