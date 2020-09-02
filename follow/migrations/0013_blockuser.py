# Generated by Django 3.1 on 2020-09-02 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200830_0128'),
        ('follow', '0012_auto_20200830_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blockuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('blocked', models.ManyToManyField(related_name='blocked', to='profiles.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='profiles.profile')),
            ],
        ),
    ]
