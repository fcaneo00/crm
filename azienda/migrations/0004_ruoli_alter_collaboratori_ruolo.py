# Generated by Django 4.1.2 on 2022-10-10 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('azienda', '0003_collaboratori_ruolo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ruoli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='collaboratori',
            name='ruolo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='azienda.ruoli'),
        ),
    ]
