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
    #validate data
    errors = Show.objects.validate(request.POST)
    if (errors):
        print ("==== errror ")
        for error in errors:
            messages.error(request, errors[error])
        print (messages)
        return redirect("/new")
    print ("===== no errors ===")
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], releasedate=request.POST['releasedate'])
    return redirect("/shows")

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")

def update(request):
    print ("------update")
    # validate data
    errors = Show.objects.validate(request.POST)
    if (errors):
        print ("==== errror ")
        for error in errors:
            messages.error(request, errors[error])
        print (messages)
        reURL = "/shows/"+ str(request.POST['id']) + "/edit"
        return redirect(reURL)
    u = Show.objects.get(id=request.POST['id'])
    u.title = request.POST['title']
    u.network = request.POST['network']
    u.releasedate = request.POST['releasedate']
    u.save()
    return redirect("/"+str(u.id))