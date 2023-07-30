from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logoutaccount, name='logoutaccount'),
    path('login/', views.loginaccount, name='loginaccount'),
    path('register/', views.registeraccount, name='registeraccount')
]
