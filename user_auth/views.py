from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'user_auth/homepage.html', {'title': 'Homepage'})

def register_user(request):
    pass