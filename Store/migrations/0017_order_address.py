# Generated by Django 5.1.2 on 2024-11-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0016_alter_comment_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
