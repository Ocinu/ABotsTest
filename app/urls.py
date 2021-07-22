from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add_new_record, name='add')
]
