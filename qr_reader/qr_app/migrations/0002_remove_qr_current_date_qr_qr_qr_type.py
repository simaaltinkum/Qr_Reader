# Generated by Django 4.2.3 on 2023-10-04 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qr',
            name='current_date',
        ),
        migrations.AddField(
            model_name='qr',
            name='qr',
            field=models.CharField(default=1, max_length=170),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qr',
            name='type',
            field=models.CharField(default=1, max_length=170),
            preserve_default=False,
        ),
    ]
