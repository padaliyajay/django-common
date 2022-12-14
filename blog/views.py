from django.shortcuts import render, reverse
from .models import Post

# Home
def index(request):
    data = dict()

    data['latest_posts'] = Post.objects.all()

    return render(request, 'blog/index.html', data)

# Post
def post(request, slug):
    data = dict()

    post = Post.objects.get(slug=slug)

    data['post'] = post

    return render(request, 'blog/post.html', data)