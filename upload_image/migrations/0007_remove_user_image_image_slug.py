# Generated by Django 3.0.2 on 2020-01-16 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload_image', '0006_auto_20200115_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_image',
            name='image_slug',
        ),
    ]
