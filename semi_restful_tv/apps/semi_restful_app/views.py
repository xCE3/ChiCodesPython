from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import *

def index(request):
    context = {
    'shows' : Show.objects.all()
    }
    return render(request, "semi_restful_app/shows.html", context)

def new(request):
    return render(request, "semi_restful_app/new.html")

def edit(request, id):
    context = {
    'show' : Show.objects.get(id=id)
    }
    return render(request, "semi_restful_app/edit.html", context)

def show(request, id):
    context = {
        'show' : Show.objects.get(id=id)
    }
    return render(request, "semi_restful_app/show.html", context)

def create(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], email=request.POST['releasedate'])
    return redirect("/shows")

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")

def update(request):
    u = Show.objects.get(id=request.POST['id'])
    u.title = request.POST['title']
    u.network = request.POST['network']
    u.releasedate = request.POST['releasedate']
    u.save()
    return redirect("/shows/"+str(u.id))