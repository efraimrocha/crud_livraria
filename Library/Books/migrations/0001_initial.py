# Generated by Django 4.2.6 on 2023-11-01 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='nome')),
                ('author', models.CharField(max_length=255, verbose_name='author')),
                ('publication_year', models.IntegerField(max_length=4, verbose_name='publication_year')),
            ],
        ),
    ]