# Generated by Django 4.2.3 on 2023-07-17 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_address_user_address2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
