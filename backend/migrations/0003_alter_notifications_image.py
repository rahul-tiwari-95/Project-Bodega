# Generated by Django 4.0.5 on 2022-07-04 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_cashflowledger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='image',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
