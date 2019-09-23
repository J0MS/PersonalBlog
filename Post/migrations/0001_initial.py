# Generated by Django 2.1.5 on 2019-09-16 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('paragraph', models.CharField(max_length=150)),
                ('image', models.ImageField(default='', null=True, upload_to='post_pictures')),
            ],
        ),
    ]
