# Generated by Django 2.1.2 on 2018-10-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0020_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]