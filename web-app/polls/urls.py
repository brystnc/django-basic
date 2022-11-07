from django.urls import path
from . import views # . == polls

urlpatterns = [
    path('', views.index, name='index')
]

