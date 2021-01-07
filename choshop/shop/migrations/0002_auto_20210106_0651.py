# Generated by Django 3.0.9 on 2021-01-06 06:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.CharField(default='', help_text='Content for description meta tag', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(default='', help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.CharField(default='', help_text='Content for description meta tag', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(default='', help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AddField(
            model_name='product',
            name='sku',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='meta_description',
            field=models.CharField(default='', help_text='Content for description meta tag', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='meta_keywords',
            field=models.CharField(default='', help_text='Comma-delimited set of SEO keywords for meta tag', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]