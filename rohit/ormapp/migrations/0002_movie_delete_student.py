# Generated by Django 5.2.1 on 2025-05-12 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('name', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('director', models.CharField(max_length=10)),
                ('hero', models.CharField(max_length=10)),
                ('your_rating', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
