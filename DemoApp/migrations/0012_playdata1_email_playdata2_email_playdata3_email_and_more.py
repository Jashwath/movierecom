# Generated by Django 5.0.4 on 2024-06-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0011_playdata1_playdata2_playdata3_publdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='playdata1',
            name='email',
            field=models.EmailField(default='/', max_length=254),
        ),
        migrations.AddField(
            model_name='playdata2',
            name='email',
            field=models.EmailField(default='/', max_length=254),
        ),
        migrations.AddField(
            model_name='playdata3',
            name='email',
            field=models.EmailField(default='/', max_length=254),
        ),
        migrations.AddField(
            model_name='publdata',
            name='email',
            field=models.EmailField(default='/', max_length=254),
        ),
    ]
