# Generated by Django 3.1 on 2020-08-28 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200828_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image_likes',
        ),
    ]
