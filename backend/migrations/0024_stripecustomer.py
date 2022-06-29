# Generated by Django 4.0.1 on 2022-06-29 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_stripecharges_stripepaymentmethodid'),
    ]

    operations = [
        migrations.CreateModel(
            name='stripeCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe', max_length=255)),
                ('email', models.CharField(default='johndoe@email.com', max_length=255)),
                ('customerID', models.CharField(max_length=500)),
                ('paymentMethodID', models.CharField(max_length=500)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('metauserID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.metauser')),
            ],
        ),
    ]
