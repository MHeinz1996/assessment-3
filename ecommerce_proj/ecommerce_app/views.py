from django.shortcuts import render
import pprint, os, json
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests as HTTP_Client

# load my apikey and secret key
load_dotenv()

# establish pretty printer
pp = pprint.PrettyPrinter(indent=2, depth=2)

def index(request):
    return render(request, 'ecommerce_app/index.html')

def home(request):
    content = [
        {
            'img': 'https://images.unsplash.com/photo-1538577880403-f9998e75dd06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Cushions',
            'price': '$19.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Sofa',
            'price': '$699.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1577979749830-f1d742b96791?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Television',
            'price': '$399.99',
        }
    ]

    return render(request, 'ecommerce_app/home.html', {'content':content, 'title': 'Home'})

def kitchen(request):
    content = [
       {
            'img': 'https://images.unsplash.com/photo-1617713780979-4ae0c726f253?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Oven',
            'price': '$399.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1583845112239-97ef1341b271?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Table Set',
            'price': '$299.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Fridge',
            'price': '$999.99',
        }
    ]

    return render(request, 'ecommerce_app/kitchen.html', {'content':content, 'title': 'Kitchen'})

def bed_bath(request):
    content = [
        {
            'img': 'https://images.unsplash.com/photo-1620641622503-43554860be67?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Sink',
            'price': '$199.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1578898887932-dce23a595ad4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Bed',
            'price': '$299.99',
        },
        {
            'img': 'https://images.unsplash.com/photo-1567002260451-50e05a6b031a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Bathtub',
            'price': '$999.99',
        }
    ]

    return render(request, 'ecommerce_app/bed_bath.html', {'content':content, 'title': 'Bed & Bath'})

@csrf_exempt
def search(request):
    # setting up my authentication with my hidden keys
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])

    if request.method == 'POST':
        body = json.loads(request.body)
        searched = body['searched']
    
    endpoint = f"http://api.thenounproject.com/icon/{searched}"

    API_response = HTTP_Client.get(endpoint, auth=auth)
    responseJSON = API_response.json()
    return JsonResponse({'img_url': responseJSON['icon']['preview_url']})
    
    # For this part, review: https://github.com/romeoplatoon/demos-and-notes/tree/master/w5d4-django-apis
    # Need to take input from search bar, and see if I can pass that into a query string or something
    # If an item that they search for is in my store, show them that item
    # If not, use the noun project to display "Sold Out" and an icon of that item they searched for



# For the cart, need to figure out how to ensure data persists using a django dictionary
# Then using that dictionary, send info to the front-end to display it on the checkout screen
# Don't think I'm allow to just use JQuery to populate an html page
# def cart(request):
