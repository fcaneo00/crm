# Generated by Django 4.1.2 on 2022-10-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azienda', '0002_collaboratori_delete_azienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboratori',
            name='ruolo',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
