# Generated by Django 4.0.5 on 2022-07-06 21:28

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_metausersocial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bodegaSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followers', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None), size=None)),
                ('following', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None), size=None)),
                ('likes', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None), size=None)),
                ('comments', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None), size=None)),
                ('productsClickedOn', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None), size=None)),
                ('unfollows', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255), size=None), size=None)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
                ('metauserID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.metauser')),
            ],
        ),
    ]
