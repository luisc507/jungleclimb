# Generated by Django 3.2.8 on 2021-11-11 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jungleapp', '0012_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
