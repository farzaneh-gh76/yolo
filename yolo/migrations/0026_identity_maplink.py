# Generated by Django 5.1 on 2024-10-19 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0025_newsletter_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='maplink',
            field=models.CharField(max_length=500, null=True, verbose_name='لینک آدرس روی نقشه '),
        ),
    ]
