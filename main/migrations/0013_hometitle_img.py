# Generated by Django 4.2.1 on 2023-05-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_hometile_hometitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometitle',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='image'),
            preserve_default=False,
        ),
    ]