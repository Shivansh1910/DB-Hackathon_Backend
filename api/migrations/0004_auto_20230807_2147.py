# Generated by Django 3.2.2 on 2023-08-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230807_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbuser',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='dbuser',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
    ]