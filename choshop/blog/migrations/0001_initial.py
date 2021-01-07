# Generated by Django 3.0.9 on 2021-01-06 18:55

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('image', models.ImageField(upload_to='media/', verbose_name='تصویر')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('meta_keywords', models.CharField(help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255)),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=255)),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('image', models.ImageField(upload_to='media/', verbose_name='تصویر')),
                ('name', models.CharField(max_length=50)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
            ],
            options={
                'verbose_name': 'زیرتگ ',
                'verbose_name_plural': 'زیرتگ ها ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('status', models.CharField(choices=[('draft', 'در حال انتظار'), ('published', 'منتشر شده')], default='draft', max_length=60, verbose_name='وضعیت')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
                ('sub_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
