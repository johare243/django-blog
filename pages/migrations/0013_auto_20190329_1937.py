# Generated by Django 2.1.7 on 2019-03-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20190329_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
