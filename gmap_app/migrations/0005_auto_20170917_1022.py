# Generated by Django 2.0 on 2017-09-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmap_app', '0004_auto_20170917_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='places',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='places',
            name='longitude',
        ),
    ]