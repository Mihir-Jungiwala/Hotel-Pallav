# Generated by Django 5.0.4 on 2024-09-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shift_Handover', '0003_remove_shift_handover_two_thousand_counts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift_handover',
            name='Update_Count',
            field=models.IntegerField(default=0),
        ),
    ]
