# Generated by Django 4.2.1 on 2023-05-09 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_verification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phoneotp',
            name='phone',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]