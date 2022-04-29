from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .choices import bedroom_choices, price_choices, state_choices


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
    ctx = {
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'state_choices': state_choices,
    }
    return render(request, 'listings/search.html', ctx)
