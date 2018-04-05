# Generated by Django 2.0.3 on 2018-04-05 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0012_auto_20180405_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited', models.BooleanField(default=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='album.Album')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-created_at',),
            },
        ),
    ]