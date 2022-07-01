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
    content = [
        {
            'img': 'https://images.unsplash.com/photo-1538577880403-f9998e75dd06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Couch Cushions',
            'price': '$19.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1583845112239-97ef1341b271?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Table Set',
            'price': '$299.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1567002260451-50e05a6b031a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Bathtub',
            'price': '$999.99',
        }
    ]

    return render(request, 'ecommerce_app/home.html', {'content':content, 'title': 'Home'})

def kitchen(request):
    content = [
       {
            'img': 'https://images.unsplash.com/photo-1538577880403-f9998e75dd06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Couch Cushions',
            'price': '$19.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1583845112239-97ef1341b271?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Table Set',
            'price': '$299.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1567002260451-50e05a6b031a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Bathtub',
            'price': '$999.99',
        }
    ]

    return render(request, 'ecommerce_app/kitchen.html', {'content':content, 'title': 'Kitchen'})

def bed_bath(request):
    content = [
        {
            'img': 'https://images.unsplash.com/photo-1538577880403-f9998e75dd06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Couch Cushions',
            'price': '$19.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1583845112239-97ef1341b271?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Table Set',
            'price': '$299.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1567002260451-50e05a6b031a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Bathtub',
            'price': '$999.99',
        }
    ]

    return render(request, 'ecommerce_app/bed_bath.html', {'content':content, 'title': 'Bed & Bath'})
