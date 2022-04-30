from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact1 = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact1.save()
        messages.success(request, 'Your request has been submitted, A realtor will get back to you soon')
        return redirect('/listing/'+listing_id)




    return