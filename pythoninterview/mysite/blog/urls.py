from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
path('', views.HomeView.as_view(), name='home'),
path('questions/', views.PostListView.as_view(), name='post_list'),
path('category/<str:category>/', views.CategoryPostListView.as_view(), name='category_post_list'),
path('difficulty/<str:difficulty>/', views.DifficultyPostListView.as_view(), name='difficulty_post_list'),
path('about/', views.AboutView.as_view(), name='about'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
