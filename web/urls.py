from django.urls import path, include
from web.views import *
urlpatterns = [
    path("", index, name="main-page")
]
