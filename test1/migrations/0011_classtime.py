# Generated by Django 2.0.3 on 2018-03-31 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0010_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='classtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JieCi', models.CharField(max_length=50)),
                ('StartTime', models.CharField(max_length=50)),
                ('StopTime', models.CharField(max_length=50)),
            ],
        ),
    ]
