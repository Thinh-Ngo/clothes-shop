# Generated by Django 3.2 on 2021-04-22 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210422_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered',
            new_name='is_ordered',
        ),
    ]
