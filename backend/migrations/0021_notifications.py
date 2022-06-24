# Generated by Django 4.0.1 on 2022-06-23 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_alter_collaboration_bid_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('image', models.FileField(default='https://bdgdaostorage.blob.core.windows.net/media/product/product_image1/white-transparent-bdga.png', upload_to='notifications/image_metadata')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('metauserID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.metauser')),
            ],
        ),
    ]
