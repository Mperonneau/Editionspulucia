# Generated by Django 2.2 on 2021-01-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulucia_web', '0010_bibliotheque1_image_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bibliotheque1',
            name='image_cover',
            field=models.ImageField(upload_to='bibliotheque'),
        ),
    ]
