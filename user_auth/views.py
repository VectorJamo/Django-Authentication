from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import forms

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(request):
    return render(request, 'user_auth/homepage.html', {'title': 'Homepage'})

def register_user(request):
    # TODO: Handle request coming from custom HTML form.
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            print(request.POST)
            form = forms.UserRegistraionForm(request.POST)
            if form.is_valid():
                print('Valid form information!')
                form.save()

                return redirect('login-user')
            else:
                print('Invalid form information')
                errors = form.errors
                for field, error_list in errors.items():
                    for error in error_list:
                        print(f"Error in {field}: {error}")
            
        form = forms.UserRegistraionForm()

        return render(request, 'user_auth/register.html', {'form': form})
