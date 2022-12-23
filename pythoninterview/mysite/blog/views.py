from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, DetailView)
from blog.models import Post
from django.db.models import Max
import random

class SearchView(ListView):
    paginate_by = 50
    model = Post
    template_name = "post_list.html"
    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search_questions')
        if query:
          questions = Post.objects.filter(title__contains=query)
          category = Post.objects.filter(category__contains=query)
          postresult = questions | category
          result = postresult
        return result


class HomeView(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    paginate_by = 50
    model = Post
    def get_queryset(self):
        return Post.objects.all().order_by('title')

class CategoryPostListView(ListView):
    paginate_by = 50
    model = Post
    def get_queryset(self, *args, **kwargs):
        category = self.kwargs.get('category')
        main_category = Post.objects.filter(category = category)
        alt_category = Post.objects.filter(alt_category = category)
        categories = main_category | alt_category
        return categories

class DifficultyPostListView(ListView):
    paginate_by = 50
    model = Post
    def get_queryset(self, *args, **kwargs):
        difficulty = self.kwargs.get('difficulty')
        return Post.objects.filter(difficulty = difficulty)

class PostDetailView(DetailView):
    model = Post

class RandomView(ListView):
    model = Post
    def get_queryset(self):
        total_posts = Post.objects.all().count()
        return Post.objects.filter(id = random.randint(1, 355))
