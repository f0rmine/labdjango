from django.test import TestCase
from django.urls import reverse
from .models import Category, Article

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(category='Test Category', slug='test-category')
        self.assertEqual(category.__str__(), 'Test Category')

class ArticleModelTest(TestCase):
    def test_article_creation(self):
        category = Category.objects.create(category='Test Category', slug='test-category')
        article = Article.objects.create(
            title='Test Article',
            description='Test Description',
            slug='test-article',
            category=category
        )
        self.assertEqual(article.__str__(), 'Test Article')

class ArticleListViewTest(TestCase):
    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)

class ArticleDetailViewTest(TestCase):
    def test_article_detail_view(self):
        category = Category.objects.create(category='Test Category', slug='test-category')
        article = Article.objects.create(
            title='Test Article',
            description='Test Description',
            slug='test-article',
            category=category
        )
        response = self.client.get(reverse('article_detail', args=[article.slug]))
        self.assertEqual(response.status_code, 200)