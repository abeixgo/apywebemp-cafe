# Generated by Django 4.2.4 on 2023-09-09 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-name_lin'], 'verbose_name': 'enlace', 'verbose_name_plural': 'enlaces'},
        ),
    ]