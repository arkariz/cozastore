# Generated by Django 3.0.3 on 2020-04-18 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pemesanan', '0006_auto_20200418_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csstags',
            name='icon1img',
        ),
        migrations.RemoveField(
            model_name='csstags',
            name='icon2img',
        ),
    ]
