from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_function(request, *args, **kwargs)
        else:
            return redirect('/accounts/login')
    return wrapper_function

def allowed_users(allowed_groups=[]):
    def decorator(view_function):
        def wrapper_function(request,*args,**kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_groups:
                return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You do not have permission to view this page')
        return wrapper_function
    return decorator