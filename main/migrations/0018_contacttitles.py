# Generated by Django 4.2.1 on 2023-05-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_contactaside'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=60, verbose_name='title 1')),
                ('title_2', models.CharField(max_length=60, verbose_name='title 2')),
                ('title_3', models.CharField(max_length=60, verbose_name='title 3')),
                ('btn_name', models.CharField(max_length=60, verbose_name='btn name')),
            ],
        ),
    ]