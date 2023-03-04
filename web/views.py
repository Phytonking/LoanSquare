from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from web.models import *
import datetime
# Create your views here.
def index(request):
    return render(request, "web/index.html")


def contact(request):
    if request.method == "POST":
        n = request.POST["Name"]
        e = request.POST["Email"]
        m = request.POST["Message"]
        mod = Message(name=n, email=e, date_sent=datetime.datetime.now(), message=m)
        mod.save()
        return render(request, "web/index.html", {"message": "Thanks for sending us a mesage, we will send you an email soon!"})

