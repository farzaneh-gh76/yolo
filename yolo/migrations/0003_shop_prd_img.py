# Generated by Django 5.1 on 2024-09-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0002_shop_prd'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_prd',
            name='img',
            field=models.ImageField(null=True, upload_to='photo'),
        ),
    ]