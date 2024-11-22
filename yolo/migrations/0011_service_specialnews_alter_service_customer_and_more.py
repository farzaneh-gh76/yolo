# Generated by Django 5.1 on 2024-10-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yolo', '0010_service_alter_employee_email_alter_employee_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='specialnews',
            field=models.CharField(max_length=100, null=True, verbose_name='خبر متحرک بالای صفحه'),
        ),
        migrations.AlterField(
            model_name='service',
            name='customer',
            field=models.IntegerField(verbose_name='تعداد مشتریان'),
        ),
        migrations.AlterField(
            model_name='service',
            name='dailyparcel',
            field=models.IntegerField(verbose_name='تعداد سفارشات روزانه'),
        ),
        migrations.AlterField(
            model_name='service',
            name='dailyview',
            field=models.IntegerField(verbose_name='تعداد بازدیدهای روزانه از سایت'),
        ),
        migrations.AlterField(
            model_name='service',
            name='follower',
            field=models.CharField(max_length=10, verbose_name='تعداد دنبال کنندگان'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option1',
            field=models.CharField(max_length=20, verbose_name='آپشن 1 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option1detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 1 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option2',
            field=models.CharField(max_length=20, verbose_name='آپشن 2 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option2detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 2 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option3',
            field=models.CharField(max_length=20, verbose_name='آپشن 3 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option3detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 3 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option4',
            field=models.CharField(max_length=20, verbose_name='آپشن 4 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option4detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 4 بالا صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option5',
            field=models.CharField(max_length=20, verbose_name='آپشن 1 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option5detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 1 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option6',
            field=models.CharField(max_length=20, verbose_name='آپشن 2 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option6detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 2 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option7',
            field=models.CharField(max_length=20, verbose_name='آپشن 3 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option7detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 3 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option8',
            field=models.CharField(max_length=20, verbose_name='آپشن 4 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='option8detail',
            field=models.CharField(max_length=50, verbose_name='جزئیات آپشن 4 پایین صفحه اصلی'),
        ),
        migrations.AlterField(
            model_name='service',
            name='rising',
            field=models.CharField(max_length=10, verbose_name='درصد رشد در سال'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service1',
            field=models.CharField(max_length=30, verbose_name='خدمت 1 صفحه درباره ما'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service1detail',
            field=models.CharField(max_length=200, verbose_name='جزئیات خدمت 1'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service2',
            field=models.CharField(max_length=30, verbose_name='خدمت 2 صفحه درباره ما'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service2detail',
            field=models.CharField(max_length=200, verbose_name='جزئیات خدمت 2'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service3',
            field=models.CharField(max_length=30, verbose_name='خدمت 3 صفحه درباره ما'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service3detail',
            field=models.CharField(max_length=200, verbose_name='جزئیات خدمت 3'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service4',
            field=models.CharField(max_length=30, verbose_name='خدمت 4 صفحه درباره ما'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service4detail',
            field=models.CharField(max_length=200, verbose_name='جزئیات خدمت 4'),
        ),
        migrations.AlterField(
            model_name='service',
            name='variety',
            field=models.IntegerField(verbose_name='تنوع محصولات'),
        ),
    ]