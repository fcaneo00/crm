# Generated by Django 4.1.2 on 2022-10-26 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intervista', '0005_alter_intervista_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intervista',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='intervista',
            name='collaboratore',
        ),
        migrations.DeleteModel(
            name='cliente',
        ),
        migrations.DeleteModel(
            name='intervista',
        ),
    ]
