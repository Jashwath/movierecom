# Generated by Django 5.0.4 on 2024-05-12 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='photo',
            field=models.BinaryField(),
        ),
    ]
