# Generated by Django 3.2.9 on 2022-03-10 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stellaris', '0002_remove_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyTraysCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/category')),
                ('description', models.TextField(max_length=500)),
                ('availability', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Party Trays Category',
            },
        ),
    ]
