# Generated by Django 5.0.4 on 2024-10-01 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_profile',
            name='Company_GST_Number',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
