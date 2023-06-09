# Generated by Django 4.1.7 on 2023-03-29 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Wilaya",
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
                    models.CharField(max_length=40, unique=True, verbose_name="Wilaya"),
                ),
                (
                    "mat",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Matricule"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=True, verbose_name="Livraison Active"),
                ),
            ],
            options={
                "verbose_name": "Wilaya",
                "verbose_name_plural": "1. Wilayas",
            },
        ),
        migrations.CreateModel(
            name="Commune",
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
                ("name", models.CharField(max_length=30, verbose_name="Commune")),
                (
                    "wilaya",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.wilaya",
                        verbose_name="Wilaya",
                    ),
                ),
            ],
            options={
                "verbose_name": "Commune",
                "verbose_name_plural": "2. Communes",
            },
        ),
    ]
