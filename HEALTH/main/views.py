from django.shortcuts import render
from .models import ContactMessage
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method =='POST':    
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get("subject")
        message = request.POST.get('message')

        # save to database
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            subject=subject,
            message=message,
        )
    return render(request, 'contact.html')

def appointment(request):
    return render(request, 'appointment.html')

def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def service(request):
    return render(request, 'service.html')

def testimonial(request):
    return render(request, 'testimonial.html')
def error(request):
     return render (request, '404.html')
