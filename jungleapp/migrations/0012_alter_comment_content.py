# Generated by Django 3.2.8 on 2021-11-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0011_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]