# Generated by Django 2.1.7 on 2019-03-30 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190330_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='intro',
        ),
    ]
