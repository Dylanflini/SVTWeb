# Generated by Django 2.2.6 on 2020-04-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posiblecliente',
            name='copiaMensaje',
            field=models.BooleanField(null=True),
        ),
    ]
