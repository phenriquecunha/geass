# Generated by Django 3.2.5 on 2021-08-03 14:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0006_alter_detour_detour'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('weight', models.IntegerField(default=1, verbose_name='Peso')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='request',
            name='type',
        ),
        migrations.CreateModel(
            name='DailyMonitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('date', models.DateField(verbose_name='Data')),
                ('current_balance', models.IntegerField(verbose_name='Saldo Atual')),
                ('open', models.IntegerField(verbose_name='Abertas')),
                ('completed', models.IntegerField(verbose_name='Concluídas')),
                ('previous_balance', models.IntegerField(verbose_name='Saldo Anterior')),
                ('type_of_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.typeofrequest', verbose_name='Tipo de solcitiação')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='request',
            name='type_of_request',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='scheduling.typeofrequest', verbose_name='Tipo de solcitiação'),
            preserve_default=False,
        ),
    ]
