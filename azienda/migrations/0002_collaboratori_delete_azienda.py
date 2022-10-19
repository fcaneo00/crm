# Generated by Django 4.1.2 on 2022-10-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collaboratori',
            fields=[
                ('codiceFiscale', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('cognome', models.CharField(max_length=50)),
                ('indirizzo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50)),
                ('cellulare', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Azienda',
        ),
    ]
