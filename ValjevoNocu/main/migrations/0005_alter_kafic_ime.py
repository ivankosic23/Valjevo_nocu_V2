# Generated by Django 5.1.6 on 2025-02-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_svirka_proslo_alter_svirka_ime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kafic',
            name='Ime',
            field=models.CharField(max_length=30),
        ),
    ]
