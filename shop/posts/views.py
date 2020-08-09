from django.shortcuts import render
from .models import Post

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        Post.objects.create(title=title, content=content)
    return redirect('main')