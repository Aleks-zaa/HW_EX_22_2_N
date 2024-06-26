# Generated by Django 5.0.6 on 2024-06-15 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0002_dog_view_counter"),
    ]

    operations = [
        migrations.CreateModel(
            name="Parent",
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
                    models.CharField(
                        help_text="Введите кличку",
                        max_length=100,
                        verbose_name="Кличка",
                    ),
                ),
                (
                    "date_born",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        help_text="Укажите дату рождения",
                        null=True,
                        verbose_name="Дата рождения",
                    ),
                ),
                (
                    "bread",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите породу",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="parentsdogs",
                        to="dogs.bread",
                        verbose_name="Порода",
                    ),
                ),
                (
                    "dog",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="parents",
                        to="dogs.dog",
                        verbose_name="Собака",
                    ),
                ),
            ],
            options={
                "verbose_name": "Собака родитель",
                "verbose_name_plural": "Собаки родители",
                "ordering": ["bread", "name"],
            },
        ),
    ]
