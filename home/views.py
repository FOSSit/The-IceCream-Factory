from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')



def contact(request):
    if request.method == 'POST':
        
        success_message = "Thank you for contacting us! We will get back to you soon."
        return render(request, 'contact.html', {'success_message': success_message})
    else:
        return render(request, 'contact.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        Contact = contact(name=name, email=email, phone=phone, desc=desc, date = date)

        Contact.save()
        #messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
