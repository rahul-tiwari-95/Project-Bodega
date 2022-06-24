# Generated by Django 4.0.1 on 2022-06-21 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_creatorsubscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creatorsubscription',
            name='stripeCustomerID',
        ),
        migrations.RemoveField(
            model_name='creatorsubscription',
            name='stripeSubscriptionID',
        ),
        migrations.AddField(
            model_name='creatorsubscription',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creatorsubscription',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
