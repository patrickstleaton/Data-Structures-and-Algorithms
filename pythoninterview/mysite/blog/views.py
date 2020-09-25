

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView)
from blog.forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Post


class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    def get_queryset(self):
        return Post.objects.all().order_by('title')

class CategoryPostListView(ListView):
    model = Post
    def get_queryset(self, *args, **kwargs):
        category = self.kwargs.get('category')
        main_category = Post.objects.filter(category = category)
        alt_category = Post.objects.filter(alt_category = category)
        categories = main_category | alt_category
        return categories

class DifficultyPostListView(ListView):
    model = Post
    def get_queryset(self, *args, **kwargs):
        difficulty = self.kwargs.get('difficulty')
        return Post.objects.filter(difficulty = difficulty)

class PostDetailView(DetailView):
    model = Post
