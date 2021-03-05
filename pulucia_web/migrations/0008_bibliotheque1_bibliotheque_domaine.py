# Generated by Django 2.2 on 2021-01-26 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pulucia_web', '0007_projet'),
    ]

    operations = [
        migrations.CreateModel(
            name='bibliotheque_domaine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caetegorie', models.SlugField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='bibliotheque1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('titre', models.CharField(max_length=90)),
                ('auteur', models.TextField(max_length=500)),
                ('document', models.FileField(upload_to='bibliotheque')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pulucia_web.bibliotheque_domaine')),
            ],
        ),
    ]
