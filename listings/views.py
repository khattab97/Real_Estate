from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .choices import bedroom_choices, price_choices, state_choices
from django.db.models import Q


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    ctx = {
        'listings': page_obj
    }
    return render(request, 'listings/listings.html', ctx)


def listing(request, listing_id):
    listing1 = get_object_or_404(Listing, pk=listing_id)
    ctx = {
        'listing': listing1
    }
    return render(request, 'listings/listing.html', ctx)


def search(request):
    listings = Listing.objects.all()

    strval = request.GET.get('keywords', False)
    if strval:
        listings = listings.filter(description__icontains=strval)

    strval = request.GET.get('city', False)
    if strval:
        listings = listings.filter(city__iexact=strval)

    strval = request.GET.get('state', False)
    if strval:
        listings = listings.filter(state__iexact=strval)

    strval = request.GET.get('bedrooms', False)
    if strval:
        listings = listings.filter(bedrooms__lte=strval)

    strval = request.GET.get('price', False)
    if strval:
        listings = listings.filter(price__lte=strval)

    ctx = {
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'state_choices': state_choices,
    'listings': listings,
    'values': request.GET,
}
    return render(request, 'listings/search.html', ctx)
