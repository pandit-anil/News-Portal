from django.urls import path
from . views import Login
from . import views

urlpatterns = [
        path('login', views.Signin, name='login'),
        path('register', views.signup, name="register"),
        path('logout',views.logout,name='logout'),
]
