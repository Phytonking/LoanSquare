from django.shortcuts import render
from django.contrib.auth import authenticate, logout

# Create your views here.
def index(request):
    return render(request, "web/index.html")

def login(request):
    if request.method == "GET":
        return render(request, "web/login.html")
    else:
        u = request.POST["username"]
        p = request.POST["password"]
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return render(reuqest, "web/index.html")
        else:
            return render(request, "web/index.html")

def register(request):
    if request.method == "GET":
        return render(request, "web/login.html")

def logout_view(request):
    logout(request)
