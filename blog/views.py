import blog
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class  PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post



def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

def postpage(request):
    return render(request, 'blog/postpage.html', {'title':'title'})