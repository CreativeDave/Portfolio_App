# Generated by Django 2.1.7 on 2019-03-29 21:46

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20190329_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectindexpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='project.ProjectCategory'),
        ),
    ]