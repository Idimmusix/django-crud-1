from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse
from blog.models import Post

# Create your views here.

class HomeView(DetailView):
  model=Post

class PostListView (ListView):
  # 'blog/Post_List.html'
  model=Post

class PostCreateView (CreateView):
  model = Post
  fields="_all_"
  success_url = reverse_lazy("blog:all")

class PostDetailView (DetailView):
  model:Post

class PostUpdateView (UpdateView):
  model = Post
  fields = "_all_"
  success_url = reverse_lazy("blog:all")

class PostDeleteView (UpdateView):
  model = Post
  fields = "_all_"
  success_url = reverse_lazy("blog:all")


