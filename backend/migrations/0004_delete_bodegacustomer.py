# Generated by Django 4.0.1 on 2022-06-30 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_customerpayment_alter_stripecharges_bodegacustomerid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bodegaCustomer',
        ),
    ]