# Generated by Django 3.2.8 on 2021-10-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_orderitem_product_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
