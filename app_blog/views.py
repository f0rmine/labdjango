from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Category

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-pub_date')
        category_slug = self.request.GET.get('category_slug')  # Отримуємо параметр з GET-запиту
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  # Передаємо список категорій у шаблон
        return context

    
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html' 
    context_object_name = 'article'
    
#class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'index.html', context=None)
