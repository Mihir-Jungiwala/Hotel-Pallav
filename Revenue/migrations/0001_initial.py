# Generated by Django 4.1.13 on 2024-04-17 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Cash_Deposite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deposite_Food_Date', models.DateField()),
                ('Deposite_Food_Time', models.TimeField()),
                ('Deposite_Food_Username', models.CharField(max_length=100)),
                ('Deposite_Food_Withdrawer', models.CharField(max_length=100)),
                ('Deposite_Food_Amount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel_Cash_Deposite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Deposite_Hotel_Date', models.DateField()),
                ('Deposite_Hotel_Time', models.TimeField()),
                ('Deposite_Hotel_Username', models.CharField(max_length=100)),
                ('Deposite_Hotel_Withdrawer', models.CharField(max_length=100)),
                ('Deposite_Hotel_Amount', models.CharField(max_length=50)),
            ],
        ),
    ]
