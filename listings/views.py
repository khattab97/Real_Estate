from django.shortcuts import render
from .models import Listing
from django.shortcuts import get_object_or_404


def index(request):
    listings = Listing.objects.all()
    ctx = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', ctx)


def listing(request, listing_id):

    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
