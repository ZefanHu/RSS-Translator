# Generated by Django 5.0.4 on 2024-05-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "translator",
            "0030_alter_azureaitranslator_content_translate_prompt_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="translated_content",
            name="new_hash",
            field=models.CharField(default="new", editable=False, max_length=39),
        ),
    ]
