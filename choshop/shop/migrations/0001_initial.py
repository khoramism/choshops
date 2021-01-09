# Generated by Django 3.0.9 on 2021-01-08 10:38

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shop.models.storages


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ChoShop', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('name', models.CharField(max_length=50)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'verbose_name': 'زیرتگ ',
                'verbose_name_plural': 'زیرتگ ها ',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('slug', models.SlugField(default='', max_length=100, verbose_name='لینک')),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('name', models.CharField(default='ghups', max_length=50)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('available', models.BooleanField(default=True)),
                ('numbers', models.PositiveSmallIntegerField()),
                ('is_finishing', models.BooleanField(default=False, verbose_name='آیا محصول در آستانه به پایان رسیدن است؟')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('video_link', models.TextField(blank=True, null=True)),
                ('media', models.FileField(blank=True, null=True, storage=shop.models.storages.ProtectedStorage, upload_to='products/')),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9)),
                ('sku', models.CharField(max_length=50)),
                ('requires_shipping', models.BooleanField(default=False)),
                ('is_digital', models.BooleanField(default=False)),
                ('inventory', models.IntegerField(default=0)),
                ('can_backorder', models.BooleanField(default=False)),
                ('category', models.ManyToManyField(to='shop.Category')),
                ('for_the_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
                ('sub_category', models.ManyToManyField(to='shop.SubCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
