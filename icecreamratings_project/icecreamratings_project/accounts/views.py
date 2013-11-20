from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    user = authenticate(assertion=request.POST['assertion'])

    print "Got User: ", user

    if user is not None:
        auth_login(request, user)

    return redirect('/')


def logout(request):
    auth_logout(request)
    return redirect('/')