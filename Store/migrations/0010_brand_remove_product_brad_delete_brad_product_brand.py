# Generated by Django 4.2.6 on 2024-06-19 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0009_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('image', models.ImageField(null=True, upload_to='Product/Brand')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='Brad',
        ),
        migrations.DeleteModel(
            name='Brad',
        ),
        migrations.AddField(
            model_name='product',
            name='Brand',
            field=models.ForeignKey(help_text='برند', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='Store.brand'),
        ),
    ]
