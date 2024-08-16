# Generated by Django 5.0.7 on 2024-08-16 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='Contents.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='replied_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replied_user_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]