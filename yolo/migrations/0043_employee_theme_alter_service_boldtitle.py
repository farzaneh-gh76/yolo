# Generated by Django 5.1 on 2024-11-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0042_service_boldtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='theme',
            field=models.CharField(choices=[('1', 'bg-theme-blue'), ('2', 'bg-theme-yellow'), ('3', 'bg-theme-orange'), ('4', 'bg-theme-pink')], default='انتخاب کنید...', max_length=30, null=True, verbose_name='تم رنگی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='boldtitle',
            field=models.CharField(max_length=200, verbose_name='عنوان درباره ما'),
        ),
    ]
