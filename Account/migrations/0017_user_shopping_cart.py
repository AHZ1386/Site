# Generated by Django 4.2.6 on 2024-05-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_brad_alter_order_status_product_brad'),
        ('Account', '0016_alter_user_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shopping_cart',
            field=models.ManyToManyField(blank=True, null=True, related_name='item', to='Store.product'),
        ),
    ]
