# Generated by Django 5.0.3 on 2024-03-22 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busres', '0002_usersdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('req_seats', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('Booked', 'booked'), ('Cancled', 'cancled')], max_length=10)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busres.booking')),
            ],
        ),
    ]
