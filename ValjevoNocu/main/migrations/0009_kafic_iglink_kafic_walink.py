# Generated by Django 5.1.6 on 2025-03-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_svirka_datum'),
    ]

    operations = [
        migrations.AddField(
            model_name='kafic',
            name='iglink',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='kafic',
            name='walink',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
