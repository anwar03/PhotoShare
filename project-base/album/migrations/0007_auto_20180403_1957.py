# Generated by Django 2.0.3 on 2018-04-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0006_image_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='album/'),
        ),
    ]
