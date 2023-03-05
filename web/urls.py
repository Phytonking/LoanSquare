from django.urls import path, include
from web.views import *
app_name="web"
urlpatterns = [
    path("", index, name="index"),
    path("contact", contact, name="contact")
]
