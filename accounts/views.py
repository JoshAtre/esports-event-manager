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
                      {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request,'loginaccount.html',
                          {'form': AuthenticationForm(),
                           'error': 'Username and password do not match'})
        else:
            login(request, user)
            return redirect('home')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)



# TODO: Should this be in accounts or elsewhere?
def home(request):
    return render(request, 'home.html')
