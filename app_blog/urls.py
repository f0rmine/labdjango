from django.urls import path
from .views import ArticleListView, ArticleDetailView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Головна сторінка
    path('articles/', ArticleListView.as_view(), name='article_list'),  # Усі статті
    path('articles/category/<slug:category_slug>/', ArticleListView.as_view(), name='articles_by_category'),  # Фільтр за категорією
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),  # Деталі статті
]