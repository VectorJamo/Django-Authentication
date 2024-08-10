from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import forms
from . import models

# Create your views here.
@login_required
def homepage(request):
    blogs = models.Blog.objects.all()

    return render(request, 'user_auth/homepage.html', {'title': 'Homepage', 'blogs': blogs})

def create_post(request):
    if request.method == 'POST':
        blog_title = request.POST['title']
        blog_body = request.POST['body']
        blog_author = request.user
        
        blog = models.Blog(title=blog_title, body=blog_body, author=blog_author)
        blog.save()
        
        return redirect('homepage')
    
    return render(request, 'user_auth/create_post.html', {'title': 'Create a post'})

def view_post(request, post_id):
    if request.method == 'POST':
        blog = models.Blog.objects.get(id=post_id)
        blog.title = request.POST['title']
        blog.body = request.POST['body']

        blog.save()

        return render(request, 'user_auth/view_post.html', {'title': 'Post information', 'blog': blog})

    blog = models.Blog.objects.get(id=post_id)
    
    return render(request, 'user_auth/view_post.html', {'title': 'Post information', 'blog': blog})

def delete_post(request, post_id, del_post_id):
    models.Blog.objects.get(id=post_id).delete()

    return redirect('homepage')

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

        return render(request, 'user_auth/register.html', {'title': 'Register', 'form': form})

def profile(request):
    if request.method == 'POST':
        updated_bio = request.POST['user-bio']

        current_user = request.user
        current_user.profile.user_bio = updated_bio

        current_user.profile.save()

    return render(request, 'user_auth/profile.html', {'title': 'User Profile'})