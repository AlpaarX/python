# Generated by Django 5.1.3 on 2024-12-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("devshortly", "0002_rename_long_url_url_url_remove_url_short_url_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="slug",
            field=models.SlugField(max_length=6, unique=True),
        ),
    ]
