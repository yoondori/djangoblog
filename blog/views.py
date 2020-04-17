from django.shortcuts import render


posts = [
    {
        'author': 'DoriLee',
        'title': 'Blog Post 1',
        'content': 'I want to study biology',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'I want to study chemistry',
        'date_posted': 'Jan 27, 2018'
    }
]

# could load the template and render it, and pass that as http response
# django has a shortcut got it - django.shortcuts, render.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'about'})