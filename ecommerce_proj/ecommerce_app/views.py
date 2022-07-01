from django.shortcuts import render
import requests, pprint, os, json
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import requests as HTTP_Client

# load my apikey and secret key
load_dotenv()

# establish pretty printer
pp = pprint.PrettyPrinter(indent=2, depth=2)

def index(request):

    # setting up my authentication with my hidden keys
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])

    return render(request, 'ecommerce_app/index.html')

def home(request):
    content = {
        'title': 'Home'
    }

    return render(request, 'ecommerce_app/home.html', content)

def kitchen(request):
    content = {
        'title': 'Kitchen'
    }

    return render(request, 'ecommerce_app/kitchen.html', content)

def bed_bath(request):
    content = {
        'title': 'Bed & Bath'
    }

    return render(request, 'ecommerce_app/bed_bath.html', content)

def office(request):
    content = {
        'title': 'Office'
    }

    return render(request, 'ecommerce_app/office.html', content)