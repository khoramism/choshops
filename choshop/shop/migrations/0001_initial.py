# Generated by Django 3.0.9 on 2021-01-02 14:23

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ChoShop', max_length=50)),
                ('loc', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='ghups', max_length=50)),
                ('summary', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='انتشار')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='ساخت')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('status', models.CharField(choices=[('available', 'موجود'), ('out', 'ناموجود')], default='draft', max_length=60, verbose_name='وضعیت')),
                ('numbers', models.PositiveSmallIntegerField()),
                ('is_finishing', models.BooleanField(default=False, verbose_name='آیا محصول در آستانه به پایان رسیدن است؟')),
                ('category', models.ManyToManyField(to='shop.Category')),
                ('for_the_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
                ('sub_category', models.ManyToManyField(to='shop.SubCategory')),
            ],
        ),
    ]