# Generated by Django 5.1 on 2024-10-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0015_blog_keyword_blog_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان مقاله'),
        ),
    ]
