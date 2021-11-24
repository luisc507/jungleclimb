# Generated by Django 3.2.8 on 2021-11-17 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0021_sectors_guidebook'),
    ]

    operations = [
        migrations.CreateModel(
            name='type_of_climb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='sectors',
            name='type_of_climb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.type_of_climb'),
        ),
        migrations.AlterField(
            model_name='routes',
            name='type_of_climb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.type_of_climb'),
        ),
    ]
