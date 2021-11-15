from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, "picApp/homepage.html")

def signIn(request):
    return render(request, "picApp/signIn.html" )

