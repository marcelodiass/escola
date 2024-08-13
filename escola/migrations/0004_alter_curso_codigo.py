# Generated by Django 5.0.3 on 2024-08-13 13:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_alter_estudante_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
