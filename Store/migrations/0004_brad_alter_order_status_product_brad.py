# Generated by Django 4.2.6 on 2024-02-04 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(null=True)),
                ('image', models.ImageField(null=True, upload_to='Product/brand')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('aw', 'در انتظار تایید'), ('p', 'درحال پردازش'), ('r', 'اماده ارسال از انبار'), ('d', 'تحویل پست داده شده')], max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='Brad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='Store.brad'),
        ),
    ]
