# Generated by Django 2.2 on 2021-04-07 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulucia_web', '0023_email_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='store_amazon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('products', models.TextField(max_length=6000)),
            ],
        ),
    ]
