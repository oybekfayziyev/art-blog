# Generated by Django 3.1 on 2020-08-28 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_bio'),
        ('post', '0008_auto_20200828_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='profiles.profile'),
        ),
    ]
