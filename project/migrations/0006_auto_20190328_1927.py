# Generated by Django 2.1.7 on 2019-03-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20190328_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='url',
            field=models.URLField(verbose_name='www.insert_link_to_project.com'),
        ),
    ]