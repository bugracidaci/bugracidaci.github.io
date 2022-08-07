from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.
tasks=[]
class YeniForm(forms.Form):
    task=forms.CharField(label="Yeni Görev")
def anasayfa(istek):
    return render(istek,"tasks/anasayfa.html",{"tasks":tasks })

def add(istek):
    if istek.method=="POST":
        form=YeniForm(istek.POST)
        if form.is_valid():
            save=form.cleaned_data["task"]
            tasks.append(save)
            return HttpResponseRedirect(('/tasks'))
        else:
            return render(istek,"tasks/add.html",{"form":form})
    return render(istek,"tasks/add.html",{"form_x":YeniForm()})