# Generated by Django 5.1 on 2024-11-15 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0029_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='img',
            field=models.ImageField(null=True, upload_to='photo', verbose_name='لوگو'),
        ),
    ]
