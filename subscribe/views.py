from django.shortcuts import render
from lottee.settings import EMAIL_HOST_USER

from . import forms
from django.core.mail import send_mail


# Create your views here.
# DataFlair #Send Email


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form': sub})


from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail


class SendFormEmail(View):

    def get(self, request):
        # Get the form data
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        # Send Email
        send_mail(
            'Subject - Django Email Testing',
            'Hello ' + name + ',\n' + message,
            'denisdolmatov2020@gmail.com',  # Admin
            [
                email,
            ]
        )

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('home')
