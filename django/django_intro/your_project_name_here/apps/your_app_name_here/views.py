from django.shortcuts import render, HttpResponse
def index(request):                
    return HttpResponse("placeholder to later display a list of all blogs")                         
    
def new(request):                
    return HttpResponse("placeholder to display a new form to create a new blog")
    
def create(request):
    ...
    return redirect('/')

def show(request):                
    return HttpResponse("placeholder to display blog number {}}") 

def edit(request, name, id):	      
    return HttpResponse("placeholder to display blog number 15") 
    
def destroy(request):
    ...
    return redirect('/')                   