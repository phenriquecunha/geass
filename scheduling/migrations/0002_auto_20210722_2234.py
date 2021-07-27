# Generated by Django 3.2.5 on 2021-07-23 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detour',
            options={},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.AlterModelOptions(
            name='technician',
            options={},
        ),
        migrations.AddField(
            model_name='detour',
            name='installations',
            field=models.IntegerField(default=0, verbose_name='Instalações'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detour',
            name='justification',
            field=models.TextField(default=0, verbose_name='Justificativa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='local',
            field=models.CharField(default=0, max_length=255, verbose_name='Localidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='note',
            field=models.TextField(default=0, verbose_name='Observação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='r_factor',
            field=models.IntegerField(default=0, verbose_name='Fator R'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.BooleanField(default=0, verbose_name='Status'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='type',
            field=models.CharField(default=0, max_length=10, verbose_name='Tipo de solicitação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default=0, max_length=255, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='telephone',
            field=models.CharField(default=0, max_length=255, verbose_name='Telefone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technician',
            name='name',
            field=models.CharField(default=0, max_length=255, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
