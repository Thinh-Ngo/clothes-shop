# Generated by Django 3.2 on 2021-04-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210422_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
