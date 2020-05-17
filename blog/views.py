from django.shortcuts import render
from .models import Post


# could load the template and render it, and pass that as http response
# django has a shortcut got it - django.shortcuts, render.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
