# Generated by Django 4.1.7 on 2023-04-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipe_direction_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
