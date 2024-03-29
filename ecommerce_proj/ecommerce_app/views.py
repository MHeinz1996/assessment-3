from django.shortcuts import render
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pprint, os, json
import requests as HTTP_Client

# load my apikey and secret key
load_dotenv()

inventory = [
    {
        'img': 'https://images.unsplash.com/photo-1538577880403-f9998e75dd06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
        'item': 'Cushions',
        'price': '20',
    },
    {
        'img': 'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'item': 'Sofa',
        'price': '700',
    },
    {
        'img': 'https://images.unsplash.com/photo-1577979749830-f1d742b96791?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'item': 'Television',
        'price': '400',
    },
    {
        'img': 'https://images.unsplash.com/photo-1617713780979-4ae0c726f253?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'item': 'Oven',
        'price': '400',
    },
    {
        'img': 'https://images.unsplash.com/photo-1583845112239-97ef1341b271?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
        'item': 'Table Set',
        'price': '300',
    },
    {
        'img': 'https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'item': 'Fridge',
        'price': '1000',
    },
    {
        'img': 'https://images.unsplash.com/photo-1620641622503-43554860be67?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'item': 'Sink',
        'price': '200',
    },
    {
        'img': 'https://images.unsplash.com/photo-1578898887932-dce23a595ad4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
        'item': 'Bed',
        'price': '300',
    },
    {
        'img': 'https://images.unsplash.com/photo-1567002260451-50e05a6b031a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
        'item': 'Bathtub',
        'price': '1000',
    }
]

# establish pretty printer
pp = pprint.PrettyPrinter(indent=2, depth=2)

def index(request):
    return render(request, 'ecommerce_app/index.html')

def home(request):
    content = [
        {
            'img': 'https://images.unsplash.com/photo-1538577880403-f9998e75dd06?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Cushions',
            'price': '20',
        },
        {
            'img': 'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Sofa',
            'price': '700',
        },
        {
            'img': 'https://images.unsplash.com/photo-1577979749830-f1d742b96791?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Television',
            'price': '400',
        }
    ]

    return render(request, 'ecommerce_app/categories.html', {'content':content, 'title': 'Home'})

def kitchen(request):
    content = [
       {
            'img': 'https://images.unsplash.com/photo-1617713780979-4ae0c726f253?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Oven',
            'price': '400',
        },
        {
            'img': 'https://images.unsplash.com/photo-1583845112239-97ef1341b271?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Table Set',
            'price': '300',
        },
        {
            'img': 'https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Fridge',
            'price': '1000',
        }
    ]

    return render(request, 'ecommerce_app/categories.html', {'content':content, 'title': 'Kitchen'})

def bed_bath(request):
    content = [
        {
            'img': 'https://images.unsplash.com/photo-1620641622503-43554860be67?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Sink',
            'price': '200',
        },
        {
            'img': 'https://images.unsplash.com/photo-1578898887932-dce23a595ad4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'item': 'Bed',
            'price': '300',
        },
        {
            'img': 'https://images.unsplash.com/photo-1567002260451-50e05a6b031a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80',
            'item': 'Bathtub',
            'price': '1000',
        }
    ]

    return render(request, 'ecommerce_app/categories.html', {'content':content, 'title': 'Bed & Bath'})

def search(request):
    # setting up my authentication with my hidden keys
    auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])

    # Get from search form
    searched = request.GET.get('searched')
    match = False
    
    # Loops through store inventory to see if searched item is in stock
    # If so, will set the content with that item's info
    # If not, will set content with Noun Project info
    # Content will be sent to front end to be displayed in a modal
    for i, item in enumerate(inventory):
        if(searched == item['item']):
            content = [inventory[i]]
            match = True
            break
    if match == False:
        endpoint = f"http://api.thenounproject.com/icon/{searched}"

        API_response = HTTP_Client.get(endpoint, auth=auth)
        responseJSON = json.loads(API_response.content)

        content = [
            {
                'img': responseJSON['icon']['preview_url'],
                'item': searched,
                'price': 'SOLD OUT!',
            }
        ]
    pp.pprint(content)
    return JsonResponse(content[0])
    
# Function will tally up the total price of the cart and display all of
# the cart_list contents and the total price to the cart.html page
def cart(request):
    total_price = 0
    content = cart_list
    for item in content:
        if item['price']:
            total_price = total_price + int(item['price'])
    return render(request, 'ecommerce_app/cart.html', {'content':content, 'title': 'Cart', 'total_price': total_price})

# When a user hits the 'Add to Cart' button, the front end sends a
# string that is in the form of a python dictionary to the backend
# The backend then parses the string and formats it into a workable
# form and adds the content of that item to the cart_list
cart_list = []
def add_to_cart(request):
    content = []
    system = request.POST.get('add-to-cart-button', None)
    temp = system.split(',')

    for item in temp:
        content.append(item.split(':'))
    print(content[0][0])
    cart_list.append({content[0][0]: content[0][1], content[1][0]: content[1][1]})
    print(cart_list)
    return HttpResponse(status=204) # Sends a 204 response since I don't need it to really do anything else

# When a page loads, the front end sends a request asking for the length
# of the cart_list. This function responds with that length
def cart_counter(request):
    return JsonResponse({'badge':len(cart_list)})