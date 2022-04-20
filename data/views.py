from django.shortcuts import render
from urllib3 import HTTPResponse

# Create your views here.

def enquiry(request):
    if request.method == 'POST':
        return HTTPResponse("Helle")