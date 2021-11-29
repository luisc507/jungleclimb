# Generated by Django 3.2.8 on 2021-11-29 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0034_remove_crags_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crags',
            name='image',
            field=models.ImageField(upload_to='post/'),
        ),
        migrations.AlterField(
            model_name='gallery_acid',
            name='image',
            field=models.ImageField(upload_to='post/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='post/'),
        ),
        migrations.AlterField(
            model_name='routes',
            name='topo',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
        migrations.AlterField(
            model_name='sectors',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]