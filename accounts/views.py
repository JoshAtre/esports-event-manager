from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect


# Create your views here.
def logoutaccount(request):        
    logout(request)
    return redirect('home')


def loginaccount(request):    
    if request.method == 'GET':
        return render(request, 'loginaccount.html', 
                      {'form':AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html', 
                    {'form': AuthenticationForm(), 
                    'error': 'username and password do not match'})
        else: 
            login(request, user)
            return redirect('home')


# TODO: Should this be in accounts or elsewhere?
def home(request):
    return render(request, 'home.html')
