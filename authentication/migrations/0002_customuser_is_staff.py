# Generated by Django 5.0.6 on 2024-07-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
