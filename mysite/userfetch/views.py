from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse("Register.")
    
def index(request):
    return HttpResponse("Hello, world. You're at the login page.")

def fetch(request):
	User.objects.create(first_name=request.POST['first_name'], 
						last_name=request.POST['last_name'], 
						email=request.POST['email'], 
						CCN=request.POST['CCN'], 
						phone=request.POST['phone'], 
						address=request.POST['address'], 
						password=request.POST['password'])
