# Generated by Django 2.2.19 on 2021-03-10 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0007_movie_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="cover",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
