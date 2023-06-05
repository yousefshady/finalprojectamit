from django.shortcuts import redirect

def notauthenticated(view_func):
    def wrapper_func(req,*args, **kwargs):
        if req.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(req,*args, **kwargs)
    return wrapper_func

def verifyrequired(view_func):
    def wrapper_func(req,*args, **kwargs):
        if req.user.verified == True:
            return view_func(req,*args, **kwargs)
        else:
            return redirect('pleaseverify')
    return wrapper_func