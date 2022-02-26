# Generated by Django 4.0.2 on 2022-02-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=250, null=True)),
                ('city', models.CharField(max_length=30, null=True, verbose_name='city')),
                ('state', models.CharField(max_length=30, null=True, verbose_name='state')),
                ('zip_code', models.CharField(max_length=30, null=True, verbose_name='zip')),
                ('country', models.CharField(max_length=30, null=True, verbose_name='country')),
                ('county', models.CharField(blank=True, max_length=30, null=True, verbose_name='county')),
                ('route', models.CharField(blank=True, max_length=30, null=True, verbose_name='route')),
                ('street_number', models.CharField(blank=True, max_length=30, null=True, verbose_name='street number')),
                ('neighborhood', models.CharField(blank=True, max_length=30, null=True, verbose_name='neighborhood')),
                ('latitude', models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True, verbose_name='longitude')),
            ],
        ),
    ]
