# Generated by Django 3.2.8 on 2021-11-16 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0019_sectors_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grades', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='routes',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='routes',
            name='order',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='routes',
            name='topo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='routes',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jungleapp.grade'),
        ),
    ]
