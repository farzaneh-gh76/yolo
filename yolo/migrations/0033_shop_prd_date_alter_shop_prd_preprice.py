# Generated by Django 5.1 on 2024-11-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0032_remove_service_option1_remove_service_option1detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_prd',
            name='date',
            field=models.DateField(auto_now=True, null=True, verbose_name='تاریخ بارگذاری'),
        ),
        migrations.AlterField(
            model_name='shop_prd',
            name='preprice',
            field=models.IntegerField(null=True),
        ),
    ]