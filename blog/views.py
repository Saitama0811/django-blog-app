from django.shortcuts import render

posts = [
    {
        "author": "Saurabh Goel",
        "title": "My First Post",
        "content": "My First Article",
        "date_posted": "20-October-2020"
    },
    {
        "author": "Shubham Goel",
        "title": "My Second Post",
        "content": "My Second Article",
        "date_posted": "21-October-2020"
    }
]

def home(request):
    context = {
        'posts_var': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')