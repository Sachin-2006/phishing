from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def index(req):
	if req.method == "GET":
		print("Username : ",req.GET['username'])
		print("Password : ",req.GET['passwrd'])
	return render(req,"index.html")
