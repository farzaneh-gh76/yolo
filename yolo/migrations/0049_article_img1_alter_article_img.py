# Generated by Django 5.1 on 2024-11-22 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0048_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img1',
            field=models.ImageField(null=True, upload_to='photo', verbose_name=' تصویر نمایشی مقاله در خانه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(upload_to='photo', verbose_name='تصویر اصلی مقاله'),
        ),
    ]