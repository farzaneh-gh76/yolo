# Generated by Django 5.1 on 2024-10-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0022_commentblog_num_alter_commentblog_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='ایمیل معتبر وارد کنید', max_length=254)),
            ],
        ),
    ]
