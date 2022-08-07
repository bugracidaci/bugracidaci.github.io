from django.urls import path
from . import views
urlpatterns=[
    #path("<str:isim>", views.selamla, name="selamla"),
    path("",views.anasayfa,name="anasayfa"),
    path("<str:isim>",views.greet,name="greet"),

]