# Generated by Django 4.2.11 on 2024-04-17 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("shopitem", "0005_secondhanditem_status_swapitem_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="secondhanditem",
            name="contacts",
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="secondhanditem",
            name="isforswap",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="secondhanditem",
            name="swapfor",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="SwapItem",
        ),
    ]
