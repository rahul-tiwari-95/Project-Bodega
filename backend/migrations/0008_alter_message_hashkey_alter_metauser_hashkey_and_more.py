# Generated by Django 4.0.1 on 2022-02-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_order_details_remove_product_product_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='hashkey',
            field=models.TextField(default='1055be9bb94735ec3f804524f24efe4c821542034ac0bd6b4ff15ff95826243d', unique=True),
        ),
        migrations.AlterField(
            model_name='metauser',
            name='hashkey',
            field=models.TextField(default='ee6dc2e94d5b4d5804c4c4077aa6923c2b1897c707ac936a9eaa8ddf479f64dd28aa8f51039fc0ec184621d91f9d4cfe380a3e1ba3d61b7b170fbf77e423bcd1', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='hashkey',
            field=models.TextField(default='2af8950f665d3e5cae9fdbb618fd9b6a46868a83', unique=True),
        ),
    ]
