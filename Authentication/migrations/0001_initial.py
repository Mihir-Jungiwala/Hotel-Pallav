# Generated by Django 4.1.13 on 2024-04-17 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forgot_password_token', models.CharField(max_length=100, null=True)),
                ('token_used', models.BooleanField(default=False)),
                ('email_sent_time', models.DateTimeField(blank=True, null=True)),
                ('activity_type', models.CharField(choices=[('Login', 'Login'), ('Logout', 'Logout')], max_length=10)),
                ('activity_time', models.DateTimeField(auto_now_add=True)),
                ('login_date', models.DateField(blank=True, null=True)),
                ('logout_date', models.DateField(blank=True, null=True)),
                ('login_time', models.TimeField(blank=True, null=True)),
                ('logout_time', models.TimeField(blank=True, null=True)),
                ('minutes_logged_in', models.CharField(blank=True, max_length=5, null=True)),
                ('password_change_time', models.DateTimeField(blank=True, null=True)),
                ('password_change_duration', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
