# Generated by Django 3.2.9 on 2022-03-10 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stellaris', '0007_alter_reservation_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='address',
            field=models.CharField(default='Catabangan Zamboanga City', max_length=150),
        ),
    ]
