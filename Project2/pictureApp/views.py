from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Hello there")

def AccountView():
    return HttpResponse("This the account page")

def SearchView():
    return HttpResponse("ThIs is the search")