from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwa):
        if request.user.is_authenticated and request.user.groups.filter(name='Administrator'):
            return redirect('/adminHome/')
        elif request.user.is_authenticated and request.user.groups.filter(name='Accountant'):
            return redirect('/generalHome/')
        else:
            return view_func(request, *args, **kwa)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwa):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwa)
            else:
                return HttpResponse("You are not authorized to view this page.")
        return wrapper_func
    return decorator