# Generated by Django 2.1.7 on 2019-03-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20190329_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='category',
            name='content',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
