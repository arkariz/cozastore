# Generated by Django 3.0.3 on 2020-04-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemesanan', '0007_auto_20200418_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csstags',
            name='gambar',
        ),
        migrations.RemoveField(
            model_name='csstags',
            name='jenis',
        ),
        migrations.AddField(
            model_name='barang',
            name='gambar',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='barang',
            name='jenis',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
