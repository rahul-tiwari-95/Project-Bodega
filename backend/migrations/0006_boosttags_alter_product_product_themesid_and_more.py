# Generated by Django 4.0.1 on 2022-06-07 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_munchiespage_munchiesvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoostTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=11)),
                ('created_at', models.DateField()),
                ('modified_at', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.metauser')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_themesID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.boosttags'),
        ),
        migrations.DeleteModel(
            name='ProductThemes',
        ),
    ]
