from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils import timezone
from .models import Post, Comment

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('post_list'))

        else:
            context["error"] = "Please enter the correct username and password for a staff account. Note that both fields may be case-sensitive."
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)


def user_logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html', {'posts': posts})


# def comment_list(request):
#     comments = Post
    