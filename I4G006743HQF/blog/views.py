from django.shortcuts import render
from django.views.generic.edit import CreateView
from blog.models import Post

# Create your views here.
class PostListView (ListView):
  model=Post

class PostCreateaView (CreateView):
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


