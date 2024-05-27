from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст Новости')
    image = models.ImageField('Картинка Поста', upload_to='post_img/')
    feature = models.BooleanField('В слайдере', default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    slug = models.SlugField('Ссылка', unique=True)
    created_ta = models.DateTimeField('Дата создания поста', default=timezone.now)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self):
        return self.title
    
    def get_link(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField('Название категории', max_length=255)
    image = models.ImageField('Картинка', upload_to='cat_img/')
    slug = models.SlugField('Ссылка', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default = timezone.now)
    text = models.TextField()

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарий'

    def __str__(self):
        return self.author.login + ' ' + self.post.title