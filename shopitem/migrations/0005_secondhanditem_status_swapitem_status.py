# Generated by Django 4.2.11 on 2024-04-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "shopitem",
            "0004_remove_secondhanditem_images_remove_swapitem_images_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="secondhanditem",
            name="status",
            field=models.CharField(default="selling", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="swapitem",
            name="status",
            field=models.CharField(default="selling", max_length=100),
            preserve_default=False,
        ),
    ]
