# Generated by Django 2.0.3 on 2018-04-03 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0008_auto_20180403_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='album',
        ),
    ]
