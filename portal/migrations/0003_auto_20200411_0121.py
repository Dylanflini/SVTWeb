# Generated by Django 2.2.6 on 2020-04-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_posiblecliente_copiamensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posiblecliente',
            name='idPosibleCliente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]