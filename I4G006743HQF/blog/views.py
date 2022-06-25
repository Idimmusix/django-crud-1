from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse

from blog.models import Post

# Create your views here.

class HomeView(DetailView):
  model = Post


class PostListView (ListView):
  # 'blog/Post_List.html'
  model = Post
  # template = "blog/post_list.html"


# I can prompt the user for login let's see if it gonna work.
class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
    # form_class = PostForm
    # …

    # def form_valid(self, form):
        # form.instance.created_by = self.request.user
        # return super().form_valid(form)

# class PostCreateView (CreateView):
  # model = Post
  fields = '__all__'
  success_url = reverse_lazy("blog:all")
  # template = "blog/post_form.html"

class PostDetailView (DetailView):
  model = Post
  template_name = "blog/post_detail.html"

class PostUpdateView (UpdateView):
  model = Post
  fields = '__all__'
  success_url = reverse_lazy("blog:all")
  # template = "blog/post_form.html"

class PostDeleteView (DeleteView):
  model = Post
  fields = '__all__'
  success_url = reverse_lazy("blog:all")
  # template = "blog/post_confirm_delete.html"


