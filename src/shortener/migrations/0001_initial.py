# Generated by Django 4.1.7 on 2023-03-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URLShortener",
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
                ("url", models.URLField()),
                ("short_url", models.CharField(max_length=6, unique=True)),
            ],
            options={
                "verbose_name": "URL Shortener",
                "verbose_name_plural": "URL Shorteners",
            },
        ),
    ]
