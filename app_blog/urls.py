from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),  # Усі статті
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='articles_by_category'),  # Фільтр за категорією
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),  # Деталі статті
]
