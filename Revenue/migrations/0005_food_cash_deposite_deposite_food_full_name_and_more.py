# Generated by Django 5.0.4 on 2024-10-03 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Revenue', '0004_food_cash_deposite_deposite_food_amount_in_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_cash_deposite',
            name='Deposite_Food_Full_Name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='hotel_cash_deposite',
            name='Deposite_Hotel_Full_Name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
