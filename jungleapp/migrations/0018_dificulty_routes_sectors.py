# Generated by Django 3.2.8 on 2021-11-16 03:13

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0017_crags_comment_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='dificulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dificulty', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='sectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=100)),
                ('overview', models.CharField(blank=True, max_length=500, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('comment_count', models.IntegerField(default=0)),
                ('crag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.crags')),
            ],
        ),
        migrations.CreateModel(
            name='routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=10)),
                ('type_of_climb', models.CharField(max_length=100)),
                ('commentary', models.CharField(blank=True, max_length=500, null=True)),
                ('crag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.crags')),
                ('dificulty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.dificulty')),
                ('sector_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.sectors')),
            ],
        ),
    ]
