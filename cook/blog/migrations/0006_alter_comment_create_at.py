# Generated by Django 4.1.7 on 2023-04-06 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]