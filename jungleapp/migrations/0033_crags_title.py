# Generated by Django 3.2.8 on 2021-11-18 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0032_sectors_route_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='crags',
            name='title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.crags'),
        ),
    ]
