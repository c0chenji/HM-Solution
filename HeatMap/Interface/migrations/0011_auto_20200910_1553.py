# Generated by Django 2.2.7 on 2020-09-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interface', '0010_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='coordinates',
            field=models.CharField(default='', max_length=1200),
        ),
        migrations.AlterField(
            model_name='direction',
            name='direction',
            field=models.CharField(max_length=648),
        ),
    ]
