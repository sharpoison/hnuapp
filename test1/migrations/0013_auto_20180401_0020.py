# Generated by Django 2.0.3 on 2018-04-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0012_course_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_table',
            name='Bjmc',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='CardID',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='Dwmc',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='Jc',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='Kcmc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='Skap',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='Skbjrs',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='Skdd',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='course_table',
            name='Zc',
            field=models.CharField(default='', max_length=5),
        ),
    ]