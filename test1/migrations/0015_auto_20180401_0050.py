# Generated by Django 2.0.3 on 2018-04-01 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0014_auto_20180401_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_table',
            name='Dwmc',
            field=models.CharField(default='', max_length=200),
        ),
    ]
