# Generated by Django 5.0.7 on 2024-08-07 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_module", "0004_productcategory_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="productinformation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=200, verbose_name="رنگ")),
                ("size", models.CharField(max_length=200, verbose_name="سایز")),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="information",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product_module.productinformation",
            ),
        ),
    ]
