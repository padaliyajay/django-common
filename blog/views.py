from django.shortcuts import render
from .models import Post

# Home
def index(request):
    data = dict()

    data['latest_posts'] = Post.objects.all()

    return render(request, 'blog/index.html', data)

# Post
def post(request, slug):
    data = dict()

    data['post'] = Post.objects.get(slug=slug)

    return render(request, 'blog/post.html', data)