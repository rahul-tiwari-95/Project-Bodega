# Generated by Django 4.0.1 on 2022-05-20 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_productmetadata_size_chart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpayment',
            name='payment_provider',
        ),
        migrations.AddField(
            model_name='userpayment',
            name='stripeAccountID',
            field=models.TextField(default='Project-Bodega Member Stripe Account ID'),
        ),
        migrations.AlterField(
            model_name='productmetadata',
            name='product_image2',
            field=models.FileField(default='https://bdgdaostorage.blob.core.windows.net/media/product/product_image1/white-transparent-bdga.png', upload_to='product/product_image2'),
        ),
        migrations.AlterField(
            model_name='productmetadata',
            name='product_image3',
            field=models.FileField(default='https://bdgdaostorage.blob.core.windows.net/media/product/product_image1/white-transparent-bdga.png', upload_to='product/product_image3'),
        ),
        migrations.AlterField(
            model_name='productmetadata',
            name='product_image4',
            field=models.FileField(default='https://bdgdaostorage.blob.core.windows.net/media/product/product_image1/white-transparent-bdga.png', upload_to='product/product_image4'),
        ),
        migrations.AlterField(
            model_name='productmetadata',
            name='size_chart',
            field=models.FileField(default='https://bdgdaostorage.blob.core.windows.net/media/product/product_image1/white-transparent-bdga.png', upload_to='product/size_chart'),
        ),
    ]
