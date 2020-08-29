# Generated by Django 3.1 on 2020-08-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20200828_0935'),
        ('post', '0006_post_image_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_likes',
            field=models.ManyToManyField(null=True, related_name='likes', to='profiles.Profile'),
        ),
    ]