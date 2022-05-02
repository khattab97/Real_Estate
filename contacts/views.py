from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

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

        if user_id:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listing/' + listing_id)

        contact1 = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact1.save()
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into admin panel for more info.',
            settings.EMAIL_HOST_USER,
            [realtor_email, 'a.khatttab97@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Your request has been submitted, A realtor will get back to you soon')
        return redirect('/listing/'+listing_id)




