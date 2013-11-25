from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt


def login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        auth_login(request, user)
    return HttpResponse('OK')

#@csrf_exempt
# def login(request):
#     user = authenticate(assertion=request.POST['assertion'])

#     if user is not None:
#         auth_login(request, user)

#     return redirect('/')


@csrf_exempt
def logout(request):
    auth_logout(request)
    return redirect('/')
