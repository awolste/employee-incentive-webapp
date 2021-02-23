# Generated by Django 3.1.2 on 2021-02-16 22:49

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogitem',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='DateTime of Last Update to Item'),
        ),
        migrations.AddField(
            model_name='sponsorcatalogitem',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='DateTime of Last Update to Item'),
        ),
        migrations.AddField(
            model_name='sponsorcompany',
            name='company_point_ratio',
            field=models.IntegerField(default=1, verbose_name='US Cents to Catalog Points Ratio'),
        ),
        migrations.AlterField(
            model_name='auditpointchange',
            name='change_time',
            field=models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='DateTime of Point Change'),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='api_item_Id',
            field=models.CharField(max_length=256, unique=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='API Link/Identifier'),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='item_description',
            field=models.CharField(max_length=256, null=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='catalogitem',
            name='item_name',
            field=models.CharField(max_length=25, null=True, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Item Name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_status_change',
            field=models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='Last DateTime of OrderStatus Update'),
        ),
    ]