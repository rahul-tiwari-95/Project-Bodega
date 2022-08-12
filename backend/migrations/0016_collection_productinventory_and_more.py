# Generated by Django 4.0.5 on 2022-07-23 20:04

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_rename_product_categoryid_product_productcategoryid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default collection', max_length=255)),
                ('description', models.CharField(default='default collection description', max_length=400)),
                ('coverImage', models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='collection/coverImage/')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('productVariant', models.TextField(default='OS')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='discount_ID',
            new_name='discountID',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='shop_ID',
            new_name='shopID',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image1',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='product/product_image1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image2',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='product/product_image2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image3',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='product/product_image3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image4',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='product/product_image4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_chart',
            field=models.FileField(default='8954256a-cc48-4d73-a863-5c8ebe3c426c.jpeg', upload_to='product/size_chart'),
        ),
        migrations.AddField(
            model_name='product',
            name='collectionID',
            field=models.ForeignKey(default=backend.models.get_sentinel_collection_id, on_delete=models.SET(backend.models.get_sentinel_collection), to='backend.collection'),
        ),
        migrations.AddField(
            model_name='product',
            name='productInventoryID',
            field=models.ForeignKey(default=backend.models.get_sentinel_productInventory_id, on_delete=models.SET(backend.models.get_sentinel_productInventory), to='backend.productinventory'),
        ),
    ]