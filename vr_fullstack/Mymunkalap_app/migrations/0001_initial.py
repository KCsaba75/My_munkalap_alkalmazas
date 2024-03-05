# Generated by Django 5.0.1 on 2024-02-23 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gepjarmu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rendszam', models.CharField(max_length=10)),
                ('gyartmany', models.CharField(max_length=255)),
                ('tipus', models.CharField(max_length=255)),
                ('gyartasi_ev', models.IntegerField()),
                ('alvazszam', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hibatipusok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hiba', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Megrendelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=255)),
                ('cim', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefon', models.IntegerField()),
                ('gepjarmu_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymunkalap_app.gepjarmu')),
            ],
        ),
        migrations.CreateModel(
            name='Munkalap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(auto_now_add=True)),
                ('utolsomodositas', models.DateField(auto_now=True)),
                ('munkalapstatus', models.CharField(choices=[('enum_value_1', 'Állapot 1'), ('enum_value_2', 'Állapot 2')], max_length=20)),
                ('munkalapszam', models.CharField(max_length=20)),
                ('kmoraallas', models.IntegerField()),
                ('uzemenyagszint', models.CharField(choices=[('enum_value_1', 'Opció 1'), ('enum_value_2', 'Opció 2')], max_length=20)),
                ('hibaleiras', models.TextField()),
                ('varhatohatarido', models.DateField()),
                ('elvegzettmunka', models.TextField()),
                ('felhasznaltanyag', models.TextField()),
                ('hibatipus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymunkalap_app.hibatipusok')),
                ('megrendelo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mymunkalap_app.megrendelo')),
            ],
        ),
    ]