# Generated by Django 4.2 on 2024-08-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Login",
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
                    "login",
                    models.CharField(max_length=255, unique=True, verbose_name="Логин"),
                ),
                ("password", models.CharField(max_length=255, verbose_name="Пароль")),
            ],
            options={
                "verbose_name": "Логин",
                "verbose_name_plural": "Логины",
            },
        ),
    ]
