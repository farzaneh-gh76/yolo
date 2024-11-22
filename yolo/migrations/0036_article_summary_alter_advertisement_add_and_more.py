# Generated by Django 5.1 on 2024-11-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0035_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=100, null=True, verbose_name='چکیده'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='add',
            field=models.CharField(max_length=30, verbose_name='عنوان تبلیغ'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='delay',
            field=models.CharField(max_length=10, verbose_name='لطفا تاخیر در نمایش را تغییر ندهید'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='exp',
            field=models.CharField(max_length=100, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='article',
            name='subject',
            field=models.CharField(max_length=10, null=True, verbose_name='موضوع مقاله'),
        ),
    ]
