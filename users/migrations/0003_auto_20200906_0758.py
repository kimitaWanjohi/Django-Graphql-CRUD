# Generated by Django 3.0.8 on 2020-09-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200906_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(default='captain_deadpool', upload_to='pics'),
        ),
    ]