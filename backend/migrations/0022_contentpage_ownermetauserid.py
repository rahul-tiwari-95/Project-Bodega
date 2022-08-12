# Generated by Django 4.0.5 on 2022-08-12 19:58

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_remove_productcategory_category_desc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='ownerMetaUserID',
            field=models.ForeignKey(default=backend.models.get_sentinel_MetaUser_id, on_delete=models.SET(backend.models.get_sentinel_MetaUser), to='backend.metauser'),
        ),
    ]