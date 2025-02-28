# Generated by Django 2.2.24 on 2021-12-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_objecttype_has_geometry"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="objecttype",
            name="has_geometry",
        ),
        migrations.AddField(
            model_name="objecttype",
            name="allow_geometry",
            field=models.BooleanField(
                default=True,
                help_text="Shows whether the related objects can have geographic coordinates. If the value is 'false' the related objects are not allowed to have coordinates and the creation/update of objects with `geometry` property will raise an error ",
                verbose_name="allow geometry",
            ),
        ),
    ]
