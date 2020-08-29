# Generated by Django 3.1 on 2020-08-28 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_bio'),
        ('follow', '0006_auto_20200828_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(default=2, related_name='followers', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='following',
            field=models.ManyToManyField(default=2, related_name='following', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='following_user', to='profiles.profile'),
        ),
    ]