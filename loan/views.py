from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from loan.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/loan/login")
def index(request):
    return render(request, "loan/index.html", {"InvestorAccount": InvestorAccount.objects.filter(owner=request.user), "BorrowerAccount": BorrowerAccount.objects.filter(owner=request.user), "AccountCount": InvestorAccount.objects.filter(owner=request.user).count()+BorrowerAccount.objects.filter(owner=request.user).count()})

def login_view(request):
    if request.method == "GET":
        return render(request, "loan/login.html")
    else:
        u = request.POST["username"]
        p = request.POST["password"]
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("loan:index"))
        else:
            return render(request, "loan/login.html", {"message": "incorrect username or password"})

def register_view(request):
    if request.method == "GET":
        return render(request, "loan/register.html")
    else:
        u = request.POST["username"]
        p = request.POST["password"]
        password_match = request.POST["password"] == request.POST["c_password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone_number = request.POST["tel"]
        verify = request.POST["verify"]
        if verify and password_match:
            l = User(username=u, password=p, email=email, first_name=first_name, last_name=last_name)
            l.save()
            BorrowerAccount(owner=User.objects.get(username=u)).save()
            return HttpResponseRedirect(reverse("loan:index"))
        else:
            return render(request, "loan/register.html", {"message": "Register did not go through, check registration details."})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("web:index"))


def account_view(request, account_number):
    try:
        k = InvestorAccount.objects.get(account_id=int(account_number), owner=request.user)
        return render(request, "loan/account.html", {"account": k})
    except InvestorAccount.DoesNotExist:
        return render(request, "loan/account.html", {"account": None})
