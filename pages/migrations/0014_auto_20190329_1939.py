# Generated by Django 2.1.7 on 2019-03-29 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20190329_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
