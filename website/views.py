from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'service.html')


def pricing(request):
    return render(request, 'pricing.html')


"""  # send email
send_mail(
message_name,  # subject
message,  # message
message_email,  # from email
['rafiq.freelancer24@gmail.com'],  # to email
)
"""
