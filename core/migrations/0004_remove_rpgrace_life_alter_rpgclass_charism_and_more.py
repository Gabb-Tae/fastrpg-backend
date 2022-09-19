# Generated by Django 4.1.1 on 2022-09-15 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_rpgclass_constitution'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rpgrace',
            name='life',
        ),
        migrations.AlterField(
            model_name='rpgclass',
            name='charism',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgclass',
            name='constitution',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgclass',
            name='dexterity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgclass',
            name='intelligence',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgclass',
            name='life',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='rpgclass',
            name='strength',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgclass',
            name='wisdom',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgrace',
            name='charism',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgrace',
            name='constitution',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgrace',
            name='dexterity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgrace',
            name='intelligence',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgrace',
            name='strength',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='rpgrace',
            name='wisdom',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)]),
        ),
    ]