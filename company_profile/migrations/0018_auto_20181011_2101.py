# Generated by Django 2.1.2 on 2018-10-11 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0017_auto_20181010_0731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Name',
            new_name='product_name',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
