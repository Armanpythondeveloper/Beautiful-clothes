# Generated by Django 4.2.1 on 2023-05-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_image', models.ImageField(upload_to='images', verbose_name='about image')),
                ('text_1', models.CharField(max_length=40, verbose_name='text 1')),
                ('text_2', models.CharField(max_length=40, verbose_name='text 2')),
                ('text_3', models.TextField(verbose_name='text 3')),
            ],
        ),
    ]
