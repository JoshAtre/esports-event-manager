from django.urls import path
from . import views

# TODO: This file is not being used currently. Look into it later

urlpatterns = [
    path('', views.events, name='events'),
    # path('<int:event_id>', views.detail, name='detail'),
]
