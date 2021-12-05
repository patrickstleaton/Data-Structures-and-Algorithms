from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
path('', views.HomeView.as_view(), name='home'),
path('questions/search/', views.SearchView.as_view(), name="search"),
path('questions/', views.PostListView.as_view(), name='post_list'),
path('questions/category/<str:category>/', views.CategoryPostListView.as_view(), name='category_post_list'),
path('questions/difficulty/<str:difficulty>/', views.DifficultyPostListView.as_view(), name='difficulty_post_list'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
