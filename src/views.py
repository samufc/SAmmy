from django.shortcuts import render, HttpResponse
from src.models import Post
# Create your views here.

def index(request):
    post=Post.objects.all()
    return render(
        request,
        'index.html',
        {'bag': post}
    )