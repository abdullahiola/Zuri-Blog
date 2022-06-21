from turtle import update
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView,UpdateView,DeleteView



from .models import Post


class PostListView(ListView):
  model= Post

class PostCreateView(CreateView):
  model=Post
  fields ="__all__"
  success_url = reverse_lazy('blog:all')

class PostDetailView(DetailView):
  model=Post

class PostUpdateView(UpdateView):
  model=Post
  fields ="__all__"
  success_url = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
  model=Post
  fields ="__all__"
  success_url = reverse_lazy('blog:all')