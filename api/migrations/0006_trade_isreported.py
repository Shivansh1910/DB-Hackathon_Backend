# Generated by Django 3.2.2 on 2023-08-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20230808_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='isReported',
            field=models.BooleanField(default=False),
        ),
    ]