# Generated by Django 4.2.1 on 2023-05-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_contactheader_alter_hometitle_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('subject', models.CharField(max_length=40, verbose_name='subject')),
                ('message', models.TextField(verbose_name='message')),
            ],
        ),
    ]
