# Generated by Django 5.1 on 2024-10-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0023_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='نام')),
                ('lname', models.CharField(max_length=30, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(help_text='ایمیل معتبر وارد کنید', max_length=254, verbose_name='آدرس ایمیل')),
                ('call', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('comment', models.TextField(verbose_name='نظر')),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]