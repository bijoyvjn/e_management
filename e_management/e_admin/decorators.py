from django.shortcuts import redirect

def signin_required(func):

    def wrapper(request,id=None,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return func(request)
    return wrapper
