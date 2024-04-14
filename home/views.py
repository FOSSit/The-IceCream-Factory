from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from home.models import Contact

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        new_contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        new_contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Redirect to the contact page after form submission

    return render(request, 'contact.html')
