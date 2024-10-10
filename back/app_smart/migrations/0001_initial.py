# Generated by Django 5.0.7 on 2024-09-27 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Temperatura', 'Temperatura'), ('Umidade', 'Umidade'), ('Contador', 'Contador'), ('Luminosidade', 'Luminosidade')], max_length=50)),
                ('mac_address', models.CharField(max_length=20, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('localizacao', models.CharField(max_length=100)),
                ('responsavel', models.CharField(max_length=100)),
            ],
        ),
    ]
