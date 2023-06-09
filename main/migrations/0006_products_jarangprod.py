# Generated by Django 4.2.1 on 2023-05-13 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_aboutpartners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=30, verbose_name='product name')),
                ('prod_teg', models.CharField(max_length=30, verbose_name='product teg')),
            ],
        ),
        migrations.CreateModel(
            name='JarangProd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='price')),
                ('line_1', models.CharField(max_length=50, verbose_name='line 1')),
                ('line_3', models.TextField(max_length=50, verbose_name='line 3')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('jarang_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
                ('review', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
