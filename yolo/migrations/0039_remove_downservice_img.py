# Generated by Django 5.1 on 2024-11-15 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0038_downservice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downservice',
            name='img',
        ),
    ]