# Generated by Django 5.1.2 on 2024-10-30 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0020_remove_user_address_useraddress_home_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='main_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_address', to='Account.useraddress'),
        ),
    ]