# Generated by Django 3.0.5 on 2020-05-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0005_channeldetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channeldetail',
            old_name='user',
            new_name='username',
        ),
    ]
