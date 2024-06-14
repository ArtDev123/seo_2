# Generated by Django 5.0.6 on 2024-06-14 06:28

import courses.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0004_content_file_image_text_video"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content",
            options={"ordering": ["order"]},
        ),
        migrations.AlterModelOptions(
            name="module",
            options={"ordering": ["order"]},
        ),
        migrations.RemoveField(
            model_name="module",
            name="created",
        ),
        migrations.RemoveField(
            model_name="module",
            name="slug",
        ),
        migrations.AddField(
            model_name="content",
            name="order",
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="module",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="module",
            name="order",
            field=courses.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
