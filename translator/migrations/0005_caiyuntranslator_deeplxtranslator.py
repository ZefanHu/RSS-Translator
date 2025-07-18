# Generated by Django 5.0.1 on 2024-01-28 08:11

import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translator", "0004_alter_openaitranslator_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="CaiYunTranslator",
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
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
                ("valid", models.BooleanField(null=True, verbose_name="Valid")),
                ("token", encrypted_model_fields.fields.EncryptedCharField()),
                (
                    "url",
                    models.URLField(
                        default="http://api.interpreter.caiyunai.com/v1/translator",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "verbose_name": "CaiYun",
                "verbose_name_plural": "CaiYun",
            },
        ),
        migrations.CreateModel(
            name="DeepLXTranslator",
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
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
                ("valid", models.BooleanField(null=True, verbose_name="Valid")),
                (
                    "deeplx_api",
                    models.CharField(
                        default="http://127.0.0.1:1188/translate", max_length=255
                    ),
                ),
            ],
            options={
                "verbose_name": "DeepLX",
                "verbose_name_plural": "DeepLX",
            },
        ),
    ]
