# Generated by Django 5.1 on 2024-11-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0045_faqs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faqs',
            old_name='gender',
            new_name='group',
        ),
        migrations.AlterField(
            model_name='faqs',
            name='answer',
            field=models.TextField(verbose_name='پاسخ '),
        ),
    ]
