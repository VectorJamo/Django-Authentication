from django.shortcuts import render
from django.http import HttpResponse

from . import forms

# Create your views here.
def homepage(request):
    return render(request, 'user_auth/homepage.html', {'title': 'Homepage'})

def register_user(request):
    # TODO: Handle request coming from custom HTML form.
    if request.method == 'POST':
        print('POST request arrived!')
        
    form = forms.UserRegistraionForm()

    return render(request, 'user_auth/register.html', {'form': form})