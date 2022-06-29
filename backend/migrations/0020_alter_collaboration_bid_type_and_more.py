# Generated by Django 4.0.1 on 2022-06-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaboration',
            name='bid_type',
            field=models.TextField(choices=[('FIXED-PAYMENT', 'FIXED-PAYMENT'), ('COMMISSION-%-ON-SALES', 'COMMISSION-%-ON-SALES'), ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')]),
        ),
        migrations.AlterField(
            model_name='collaboration',
            name='creator_collab_choice',
            field=models.TextField(choices=[('FIXED-PAYMENT', 'FIXED-PAYMENT'), ('COMMISSION-%-ON-SALES', 'COMMISSION-%-ON-SALES'), ('FREE-HELP-FROM-THE-COMMUNITY', 'FREE-HELP-FROM-THE-COMMUNITY')]),
        ),
    ]
