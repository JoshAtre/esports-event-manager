from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
def registeraccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #aw_password = form.cleaned_data.get('<PASSWORD>')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('loginaccount')
    else:
        form = UserCreationForm()
    
    return render(request, 'registeraccount.html', {'form': form})

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
