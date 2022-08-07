from django.shortcuts import render
import datetime
# Create your views here.
def anasayfa(istek):
    now=datetime.datetime.now()
    return render(istek,"newyear/anasayfa.html",{
        "newyear":now.month ==8 and now.day == 7
    })
