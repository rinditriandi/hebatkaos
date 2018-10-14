# Generated by Django 2.1.2 on 2018-10-13 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_profile', '0023_quality'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'Tentang Kami'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Hubungi Kami'},
        ),
        migrations.AlterModelOptions(
            name='gallerycategory',
            options={'verbose_name': 'Kategori Galeri'},
        ),
        migrations.AlterModelOptions(
            name='quality',
            options={'verbose_name': 'Kualitas Kaos'},
        ),
        migrations.RemoveField(
            model_name='quality',
            name='slug',
        ),
    ]
