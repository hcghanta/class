from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcome_page(request):
    return render(request,'account/welcome.html',{'section':welcome_page})

def success(request):
    return render(request, 'account/success.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated Sucessfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html',{'form':form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

	
def contact(request):
    return render(request, 'account/contact.html', {'section':contact})

def about(request):
    return render(request, 'account/about.html', {'section': about})

def help(request):
    return render(request, 'account/help.html', {'section': help})
	
