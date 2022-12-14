# Generated by Django 4.1.2 on 2022-10-10 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intervista', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='id',
        ),
        migrations.AddField(
            model_name='cliente',
            name='codiceFiscale',
            field=models.CharField(default=0, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='intervista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commento', models.CharField(max_length=1000)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intervista.cliente')),
            ],
        ),
    ]
