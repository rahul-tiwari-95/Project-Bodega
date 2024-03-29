# Generated by Django 4.0.5 on 2022-11-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_bodegaannouncementbanner_covermedia1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodegasupport',
            name='message',
        ),
        migrations.AddField(
            model_name='bodegasupport',
            name='bodegaReply',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegasupport',
            name='bodegaReplyMedia',
            field=models.FileField(blank=True, upload_to='bodegaSupport/bodegaReplyMedia'),
        ),
        migrations.AddField(
            model_name='bodegasupport',
            name='customerMessage',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='bodegasupport',
            name='customerMessageMedia',
            field=models.FileField(blank=True, upload_to='bodegaSupport/customerMessageMedia'),
        ),
    ]
