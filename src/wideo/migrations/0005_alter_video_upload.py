# Generated by Django 4.1.9 on 2024-01-23 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wideo", "0004_alter_video_upload"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="upload",
            field=models.ForeignKey(
                help_text="The uploaded video file; its resolution should be a standard one to avoid issues (e.g. 1280x720, 1920x1080...)",
                on_delete=django.db.models.deletion.PROTECT,
                to="wideo.uploadedvideo",
                verbose_name="file",
            ),
        ),
    ]
