# Generated by Django 4.0.5 on 2022-07-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_metausertags_coverbio1_metausertags_coverbio2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='yerrrcollaboration',
            name='campaignCoverImage',
            field=models.FileField(default='https://projectbodegadb.blob.core.windows.net/media/yerrrCoverImage.gif', upload_to='yerrrCoverImage/campaignCoverImage'),
        ),
    ]