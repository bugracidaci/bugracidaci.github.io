from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def anasayfa(istek):
    return  render(istek,"hello/anasayfa.html")

def selamla(istek,isim):
    return HttpResponse(f"merhaba {isim}")

def greet(istek,isim):
    return render(istek,"hello/greet.html",{"isim":isim.capitalize()})