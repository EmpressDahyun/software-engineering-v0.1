# Generated by Django 3.2.9 on 2022-03-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stellaris', '0005_auto_20220310_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='phone_number',
            field=models.PositiveIntegerField(max_length=11),
        ),
    ]
