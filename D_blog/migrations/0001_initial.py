# Generated by Django 4.2.7 on 2024-04-24 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст Новости')),
                ('image', models.ImageField(upload_to='post_img/', verbose_name='Картинка Поста')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('created_ta', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания поста')),
            ],
        ),
    ]