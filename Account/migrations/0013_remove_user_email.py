# Generated by Django 4.2.6 on 2024-04-11 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0012_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
