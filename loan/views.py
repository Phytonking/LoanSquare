from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from loan.models import *

# Create your views here.
def index(request):
    return render(request, "loan/login.html")

def login(request):
    if request.method == "GET":
        return render(request, "loan/login.html")
    else:
        u = request.POST["username"]
        p = request.POST["password"]
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return render(request, "loan/index.html")
        else:
            return render(request, "loan/index.html")

def register(request):
    if request.method == "GET":
        return render(request, "loan/login.html")

def logout_view(request):
    logout(request)
