# Generated by Django 4.2.11 on 2024-04-17 07:48

from django.db import migrations, models
import django.utils.timezone
import shopitem.models


class Migration(migrations.Migration):

    dependencies = [
        ("shopitem", "0003_itemimage_remove_secondhanditem_images_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="secondhanditem",
            name="images",
        ),
        migrations.RemoveField(
            model_name="swapitem",
            name="images",
        ),
        migrations.DeleteModel(
            name="ItemImage",
        ),
        migrations.AddField(
            model_name="secondhanditem",
            name="images",
            field=models.ImageField(
                default=django.utils.timezone.now,
                upload_to=shopitem.models.item_image_path,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="swapitem",
            name="images",
            field=models.ImageField(
                default=django.utils.timezone.now,
                upload_to=shopitem.models.item_image_path,
            ),
            preserve_default=False,
        ),
    ]
