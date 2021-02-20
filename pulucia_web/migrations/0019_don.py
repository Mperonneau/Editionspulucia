# Generated by Django 2.2 on 2021-02-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulucia_web', '0018_delete_don'),
    ]

    operations = [
        migrations.CreateModel(
            name='don',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('projet', models.CharField(max_length=400)),
                ('nom', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('montant', models.CharField(max_length=100)),
            ],
        ),
    ]