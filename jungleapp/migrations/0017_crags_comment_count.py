# Generated by Django 3.2.8 on 2021-11-15 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0016_alter_commentcrag_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='crags',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]