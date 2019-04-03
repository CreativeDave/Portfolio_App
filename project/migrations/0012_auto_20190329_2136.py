# Generated by Django 2.1.7 on 2019-03-29 21:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('project', '0011_projectpagerelatedlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectIndexPageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='index_gallery_images', to='project.ProjectIndexPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='projectcategory',
            name='icon',
        ),
        migrations.AlterField(
            model_name='projectcategory',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]