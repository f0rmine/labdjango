from django.db import models
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(u'Категорія', max_length=250, help_text=u'Максимум 250 символів')
    slug = models.SlugField(u'Слаг', default='')

    class Meta:
        verbose_name = u'Категорія для новини'
        verbose_name_plural = u'Категорії для новин'

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(u'Заголовок', max_length=250, help_text=u'Максимум 250 символів')
    description = models.TextField(blank=True, verbose_name=u'Опис')
    pub_date = models.DateTimeField(u'Дата публікації', default=timezone.now)
    slug = models.SlugField(u'Слаг', unique_for_date='pub_date')
    main_page = models.BooleanField(u'Головна', default=False, help_text=u'Показувати на головній сторінці')
    category = models.ForeignKey(Category, related_name='articles', blank=True, null=True,
                                 verbose_name=u'Категорія', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pub_date']
        verbose_name = u'Стаття'
        verbose_name_plural = u'Статті'

    def __str__(self):
        return self.title
class ArticleImage(models.Model):
    article = models.ForeignKey(Article, verbose_name=u'Стаття', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(u'Фото', upload_to='photos')
    title = models.CharField(u'Заголовок', max_length=250, help_text=u'Максимум 250 символів', blank=True)

    class Meta:
        verbose_name = u'Фото для статті'
        verbose_name_plural = u'Фото для статті'

    def __str__(self):
        return self.title
