# Generated by Django 2.1.7 on 2019-03-31 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0015_auto_20190331_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]