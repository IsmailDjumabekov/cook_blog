# Generated by Django 4.1.7 on 2023-04-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
