# Generated by Django 2.1.2 on 2018-10-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0018_auto_20181011_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
