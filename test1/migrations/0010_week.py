# Generated by Django 2.0.3 on 2018-03-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0009_troubleevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekid', models.IntegerField()),
                ('Tdate', models.CharField(max_length=50)),
            ],
        ),
    ]
