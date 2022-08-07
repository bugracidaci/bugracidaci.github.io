from django.urls import path
from . import views

urlpatterns=[
    path("",views.anasayfa,name="anasayfa"),
    path("/add",views.add,name="add")
]