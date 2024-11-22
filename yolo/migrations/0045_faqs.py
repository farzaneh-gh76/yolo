# Generated by Django 5.1 on 2024-11-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0044_alter_employee_theme'),
    ]

    operations = [
        migrations.CreateModel(
            name='faqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='پرسش')),
                ('answer', models.CharField(max_length=500, verbose_name='پاسخ ')),
                ('gender', models.CharField(choices=[('1', 'مشکلات پرداخت'), ('2', 'تحویل سفارش'), ('3', ' عمومی')], default='انتخاب کنید...', max_length=30, verbose_name='دسته بندی')),
            ],
        ),
    ]