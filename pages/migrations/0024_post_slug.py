# Generated by Django 2.1.7 on 2019-04-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
