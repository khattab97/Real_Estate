from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, price_choices, state_choices
from django.http import HttpResponse


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    ctx = {
        'listings': listings,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
         'state_choices': state_choices,
   }
    return render(request, 'pages/index.html', ctx)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    ctx = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request, 'pages/about.html', ctx)
