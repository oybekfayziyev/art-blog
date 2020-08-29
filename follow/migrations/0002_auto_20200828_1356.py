# Generated by Django 3.1 on 2020-08-28 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_bio'),
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='following',
            field=models.ManyToManyField(related_name='following', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='following',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_user', to='profiles.profile'),
        ),
    ]