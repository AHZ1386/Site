# Generated by Django 4.2.6 on 2024-06-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0017_user_shopping_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
