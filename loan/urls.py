from django.urls import path
from loan.views import *
app_name = "loan"
urlpatterns = [
    path("", index, name="index"),
    path("login", login_view, name="login_view"),
    path("register", register_view, name="register"),
    path("logout", logout_view, name="logout")
    
]
