# Generated by Django 2.0.3 on 2018-04-03 20:35

import album.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0007_auto_20180403_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=album.models.get_image_filename),
        ),
    ]
