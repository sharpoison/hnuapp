# Generated by Django 2.0.3 on 2018-03-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_auto_20180313_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='otsteam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('ImgName', models.CharField(max_length=50)),
            ],
        ),
    ]
