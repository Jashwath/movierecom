# Generated by Django 5.0.4 on 2024-05-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0004_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='time',
            field=models.IntegerField(default='0'),
        ),
    ]
