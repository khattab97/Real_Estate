from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You Are Now Logged IN')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('accounts:login')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('pages:index')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Exists')
                return redirect('accounts:register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username exists')
                return redirect('accounts:register')
            else:
                user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                # auth.login(request, user)
                # messages.success(request, 'You Are Now Logged In')
                # return redirect('pages:index')
                user.save()
                messages.success(request, 'You Are Now Registered, You Can Log In')
                return redirect('accounts:login')


        else:
            messages.error(request, 'Password Do Not Match')
            return redirect('accounts:register')

    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    ctx = {
        'contacts': contacts,
    }
    return render(request, 'accounts/dashboard.html', ctx)
