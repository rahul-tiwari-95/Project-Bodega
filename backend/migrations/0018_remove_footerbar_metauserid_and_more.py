# Generated by Django 4.0.5 on 2022-07-24 20:59

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_contentpage_textpage_websitesitemapconfig_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footerbar',
            name='metauserID',
        ),
        migrations.RemoveField(
            model_name='navigationbar',
            name='metauserID',
        ),
        migrations.AddField(
            model_name='websitesitemapconfig',
            name='footerBarID',
            field=models.ForeignKey(default=backend.models.get_sentinel_footerBar_id, on_delete=models.SET(backend.models.get_sentinel_footerBar), to='backend.footerbar'),
        ),
        migrations.AddField(
            model_name='websitesitemapconfig',
            name='navigationBarID',
            field=models.ForeignKey(default=backend.models.get_sentinel_navBar_id, on_delete=models.SET(backend.models.get_sentinel_navBar), to='backend.navigationbar'),
        ),
    ]