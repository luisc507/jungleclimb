# Generated by Django 3.2.8 on 2021-11-20 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0033_crags_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crags',
            name='title',
        ),
    ]
