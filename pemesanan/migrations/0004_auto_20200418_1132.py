# Generated by Django 3.0.3 on 2020-04-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemesanan', '0003_csstags'),
    ]

    operations = [
        migrations.AddField(
            model_name='csstags',
            name='blocktextchild1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='csstags',
            name='blocktextchild2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='csstags',
            name='btn',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='csstags',
            name='icon1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='csstags',
            name='icon1img',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='csstags',
            name='icon2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='csstags',
            name='icon2img',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
