from django.contrib import admin
from .models import Article, ArticleImage, Category
from .forms import ArticleImageForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')
    prepopulated_fields = {'slug': ('category',)}
    list_filter = ('category',) 
    search_fields = ('category',) 

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    form = ArticleImageForm
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page', 'category')
    list_filter = ('category', 'main_page')  
    search_fields = ('title', 'description')
    inlines = [ArticleImageInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)