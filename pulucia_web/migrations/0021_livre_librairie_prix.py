# Generated by Django 2.2 on 2021-02-13 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulucia_web', '0020_auto_20210213_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre_librairie',
            name='prix',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
