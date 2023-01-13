# Generated by Django 4.1.1 on 2022-12-14 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Faculte",
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
                ("libfac", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Etudiant",
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
                ("nom", models.CharField(blank=True, max_length=50, null=True)),
                ("postnom", models.CharField(blank=True, max_length=50, null=True)),
                ("prenom", models.CharField(blank=True, max_length=50, null=True)),
                ("telephone", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "faculte",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="crud.faculte"
                    ),
                ),
            ],
        ),
    ]