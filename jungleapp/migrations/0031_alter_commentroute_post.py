# Generated by Django 3.2.8 on 2021-11-17 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0030_alter_commentroute_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentroute',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsroute', to='jungleapp.routes'),
        ),
    ]