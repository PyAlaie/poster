# Generated by Django 3.2.14 on 2022-08-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20220804_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='/media/avatar.png', null=True, upload_to='avatars'),
        ),
    ]
