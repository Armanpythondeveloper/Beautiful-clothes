# Generated by Django 4.2.1 on 2023-05-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_indexheader_delete_hometitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_title', models.CharField(max_length=100, verbose_name='home title')),
                ('home_1', models.CharField(max_length=100, verbose_name='home 1')),
                ('home_2', models.CharField(max_length=100, verbose_name='home 2')),
                ('home_3', models.CharField(max_length=100, verbose_name='home 3')),
                ('home_4', models.CharField(max_length=100, verbose_name='home 4')),
                ('home_5', models.CharField(max_length=100, verbose_name='home 5')),
                ('home_6', models.CharField(max_length=100, verbose_name='home 6')),
                ('home_7', models.CharField(max_length=100, verbose_name='home 7')),
                ('home_8', models.CharField(max_length=100, verbose_name='home 8')),
                ('home_image', models.ImageField(upload_to='', verbose_name='home image')),
                ('home_footer_1', models.CharField(max_length=100, verbose_name='home footer')),
                ('home_footer_2', models.CharField(max_length=100, verbose_name='home footer_2')),
                ('home_footer_3', models.CharField(max_length=100, verbose_name='home footer_3')),
            ],
        ),
    ]
