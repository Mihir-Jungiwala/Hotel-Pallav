# Generated by Django 5.0.4 on 2024-06-29 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bill_Master', '0009_bill_master_add_bill_bill_master_debit_bill_date_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill_master_add_bill',
            name='Bill_Master_Debit_Bill_Date_5',
        ),
        migrations.RemoveField(
            model_name='bill_master_add_bill',
            name='Bill_Master_Debit_Food_Amount_5',
        ),
        migrations.RemoveField(
            model_name='bill_master_add_bill',
            name='Bill_Master_Debit_Food_Mode_Of_Payment_5',
        ),
        migrations.RemoveField(
            model_name='bill_master_add_bill',
            name='Bill_Master_Debit_Hotel_Amount_5',
        ),
        migrations.RemoveField(
            model_name='bill_master_add_bill',
            name='Bill_Master_Debit_Hotel_Mode_Of_Payment_5',
        ),
    ]
