# Generated by Django 5.0.4 on 2024-06-03 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0010_delete_apreg_delete_candidate_delete_pollsap_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='playdata1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=10)),
                ('movie_type', models.CharField(max_length=50)),
                ('actors', models.TextField()),
                ('plot', models.TextField()),
                ('poster', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='playdata2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=10)),
                ('movie_type', models.CharField(max_length=50)),
                ('actors', models.TextField()),
                ('plot', models.TextField()),
                ('poster', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='playdata3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=10)),
                ('movie_type', models.CharField(max_length=50)),
                ('actors', models.TextField()),
                ('plot', models.TextField()),
                ('poster', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='publdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=10)),
                ('movie_type', models.CharField(max_length=50)),
                ('actors', models.TextField()),
                ('plot', models.TextField()),
                ('poster', models.URLField()),
            ],
        ),
    ]
