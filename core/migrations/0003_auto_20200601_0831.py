# Generated by Django 3.0.6 on 2020-06-01 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200528_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
    ]