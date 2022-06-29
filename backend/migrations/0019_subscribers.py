# Generated by Django 4.0.1 on 2022-06-21 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_remove_creatorsubscription_stripecustomerid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerID', models.CharField(max_length=400)),
                ('priceID', models.CharField(max_length=400)),
                ('subscriptionID', models.CharField(max_length=400)),
                ('productID', models.CharField(max_length=400)),
                ('amount', models.IntegerField(default=0)),
                ('invoiceID', models.CharField(max_length=400)),
                ('status', models.CharField(max_length=400)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('metauserID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.metauser')),
            ],
        ),
    ]
