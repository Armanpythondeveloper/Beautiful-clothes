# Generated by Django 4.2.1 on 2023-05-14 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_homecontent_delete_homeproducttitle_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=40, verbose_name='title 1')),
                ('title_2', models.CharField(max_length=40, verbose_name='title 2')),
            ],
        ),
    ]
