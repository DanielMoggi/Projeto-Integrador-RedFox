# Generated by Django 4.2.7 on 2023-11-25 23:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("RedFox", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingresso",
            name="preco",
            field=models.IntegerField(default=0),
        ),
    ]