# Generated by Django 2.2 on 2021-01-24 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pulucia_web', '0003_remove_livre_librairie_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre_librairie',
            name='categorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pulucia_web.librairie_categorie'),
        ),
    ]
