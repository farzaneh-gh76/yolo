# Generated by Django 5.1 on 2024-09-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_prd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('preprice', models.IntegerField()),
                ('curprice', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]