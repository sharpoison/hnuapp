# Generated by Django 2.0.3 on 2018-03-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0004_classstatus_cardname'),
    ]

    operations = [
        migrations.AddField(
            model_name='otsteam',
            name='Tel',
            field=models.CharField(default='', max_length=50),
        ),
    ]
