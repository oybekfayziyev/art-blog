# Generated by Django 3.1 on 2020-08-29 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0009_auto_20200828_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
