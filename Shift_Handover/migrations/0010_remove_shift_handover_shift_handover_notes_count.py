# Generated by Django 5.1.5 on 2025-02-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shift_Handover', '0009_shift_handover_shift_handover_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift_handover',
            name='Shift_Handover_Notes_Count',
        ),
    ]
