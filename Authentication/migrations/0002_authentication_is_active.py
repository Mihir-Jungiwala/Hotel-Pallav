# Generated by Django 5.0.4 on 2024-09-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authentication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
