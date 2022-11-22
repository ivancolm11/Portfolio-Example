# Generated by Django 4.1.3 on 2022-11-14 19:18

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(verbose_name=500)),
                ('image', models.ImageField(upload_to='blog/images')),
                ('date', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]
