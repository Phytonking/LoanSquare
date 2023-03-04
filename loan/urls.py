from django.contrib import admin
from django.urls import path, include
from loan.views import *
app_name = "loan"
urlpatterns = [
    path("", index, name="index"),
]
