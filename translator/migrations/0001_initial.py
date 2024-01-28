# Generated by Django 4.2.9 on 2024-01-23 22:14

from django.db import migrations, models
import encrypted_model_fields.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeepLTranslator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('api_key', encrypted_model_fields.fields.EncryptedCharField()),
            ],
            options={
                'verbose_name': 'DeepL',
                'verbose_name_plural': 'DeepL',
            },
        ),
        migrations.CreateModel(
            name='MicrosoftTranslator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('api_key', encrypted_model_fields.fields.EncryptedCharField()),
                ('location', models.CharField(max_length=100)),
                ('endpoint', models.CharField(default='https://api.cognitive.microsofttranslator.com', max_length=255)),
            ],
            options={
                'verbose_name': 'Microsoft Translator',
                'verbose_name_plural': 'Microsoft Translator',
            },
        ),
        migrations.CreateModel(
            name='OpenAITranslator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('valid', models.BooleanField(null=True, verbose_name='Valid')),
                ('api_key', encrypted_model_fields.fields.EncryptedCharField()),
                ('model', models.CharField(default='gpt-3.5-turbo', max_length=100)),
                ('prompt', models.TextField(
                    default='Translate the following to {target_language},only returns translations.\n{text}')),
                ('temperature', models.FloatField(default=0.5)),
                ('max_tokens', models.IntegerField(default=1000)),
            ],
            options={
                'verbose_name': 'OpenAI',
                'verbose_name_plural': 'OpenAI',
            },
        ),
        migrations.CreateModel(
            name='Translated_Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.BinaryField(max_length=8, unique=True)),
                ('original_content', models.TextField()),
                ('translated_language', models.CharField(max_length=255)),
                ('translated_content', models.TextField()),
                ('tokens', models.IntegerField(default=0)),
                ('characters', models.IntegerField(default=0)),
            ],
        ),
    ]