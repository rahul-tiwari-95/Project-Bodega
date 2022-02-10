# Generated by Django 4.0.1 on 2022-02-08 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_product_variants_remove_metauser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField(default=0.0)),
                ('created_at', models.DateField()),
                ('modified_at', models.DateTimeField()),
                ('payment_info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.user_payment')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_active',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_hidden',
        ),
        migrations.AddField(
            model_name='shop',
            name='address_line1',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='address_line2',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='address_state',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='city',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='country',
            field=models.TextField(choices=[('INDIA', 'IN'), ('USA', 'US')], default='US'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='postal_code',
            field=models.TextField(default='201303'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_logo',
            field=models.FileField(default=None, upload_to='shop-details/profile_picture'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_type',
            name='explore_bodega_preferences',
            field=models.TextField(choices=[('Exploring-Fashion/Music', 'Exploring-Fashion/Music'), ('Exploring-Digital-Art', 'Exploring-Digital-Art'), ('Surprise-Me', 'Suprise-Me')], default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_type',
            name='feedback_bodega',
            field=models.TextField(choices=[('ITS-CONFUSING', 'ITS-CONFUSING'), ('NO-OPINION-YET', 'NO-OPINION-YET'), ('IT-EXCITES-ME', 'IT-EXCITES-ME')], default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_type',
            name='member_feedback_preferences',
            field=models.TextField(default='Cant find what you love? Type away and we will get to work!'),
        ),
        migrations.AlterField(
            model_name='message',
            name='hashkey',
            field=models.TextField(default='131e413bbe0bf615864d697748281b3fa7424db8970fa20e67f22705c19446b3', unique=True),
        ),
        migrations.AlterField(
            model_name='metauser',
            name='email',
            field=models.EmailField(default='fakeemailaddress@somewebsite.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='metauser',
            name='hashkey',
            field=models.TextField(default='72a5cea537af23ca14b30321b1d2e23345738873fa8b9eb8a886b704c170d20a7ac93cf852759ca047b81c6350e21922eaab110553b6cd665a1b7b597fa7f6db', unique=True),
        ),
        migrations.AlterField(
            model_name='metauser',
            name='password',
            field=models.TextField(default='Go for easy 4-digit numeric code - which is not obvious.', unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.metauser'),
        ),
        migrations.AlterField(
            model_name='product',
            name='hashkey',
            field=models.TextField(default='c73e7177850c9f927b61c4bbba9dedd855d5a174', unique=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='country',
            field=models.TextField(choices=[('INDIA', 'IN'), ('USA', 'US')]),
        ),
        migrations.CreateModel(
            name='Shopping_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField(default=0.0)),
                ('created_at', models.DateField()),
                ('modified_at', models.DateTimeField()),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.metauser')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateField()),
                ('modified_at', models.DateTimeField()),
                ('order_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.order_details')),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanity', models.IntegerField(default=0)),
                ('created_at', models.DateField()),
                ('modified_at', models.DateTimeField()),
                ('product_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.product')),
                ('session_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.shopping_session')),
            ],
        ),
    ]
