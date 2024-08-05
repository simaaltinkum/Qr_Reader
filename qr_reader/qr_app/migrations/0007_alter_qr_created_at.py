# Generated by Django 4.2.3 on 2024-05-23 12:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("qr_app", "0006_remove_qr_publish_date_qr_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qr",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
