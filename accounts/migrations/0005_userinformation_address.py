# Generated by Django 3.1.2 on 2021-02-23 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userinformation_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='address',
            field=models.CharField(default='N/A', max_length=100, verbose_name='Address'),
        ),
    ]