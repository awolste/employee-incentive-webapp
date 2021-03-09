# Generated by Django 3.1.2 on 2021-03-04 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('accounts', '0002_auto_20210304_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sponsor_catalog_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.sponsorcatalogitem'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='address',
            field=models.CharField(blank=True, default='N/A', max_length=100, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='approving_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.userinformation'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='license_number',
            field=models.CharField(blank=True, default='N/A', max_length=20, verbose_name='License'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=20, verbose_name='State'),
        ),
        migrations.DeleteModel(
            name='CatalogItem',
        ),
        migrations.DeleteModel(
            name='CatalogItemImage',
        ),
        migrations.DeleteModel(
            name='SponsorCatalogItem',
        ),
    ]
