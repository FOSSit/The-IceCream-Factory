from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from home.models import ContactMessage
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        Name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact_message=ContactMessage(name=Name, email=email, phone=phone, desc=desc, date = date)

        contact_message.save()
        messages.success(request, 'Your message has been sent!')
        return HttpResponse("<h1>submited sucessfully</h1>")
    return render(request, 'contact.html')
