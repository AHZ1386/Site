# Generated by Django 5.1.2 on 2024-10-30 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0021_user_main_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='main_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_address', to='Account.useraddress'),
        ),
    ]