# Generated by Django 4.0.5 on 2022-10-12 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_product_producdescription_alter_product_shopid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shopID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.shop'),
        ),
    ]
