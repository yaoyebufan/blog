# Generated by Django 2.0.7 on 2018-08-03 01:09

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_auto_20180802_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
