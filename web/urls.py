from django.urls import path, include
from web.views import *
urlpatterns = [
    path("", index, name="main-page"),
    path("contact", contact, name="contact")
]
