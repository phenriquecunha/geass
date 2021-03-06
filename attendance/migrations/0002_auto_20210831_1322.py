# Generated by Django 3.2.5 on 2021-08-31 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scheduling', '0003_auto_20210826_1324'),
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='sent_from',
            field=models.CharField(choices=[('A', 'ANDAMENTO'), ('AC', 'AGUARDANDO CONTATO'), ('AF', 'AGUARDADO FECHAMENTO'), ('EA', 'EM ANALISE'), ('CH', 'CHAT')], max_length=255, null=True, verbose_name='Encaminhado de'),
        ),
        migrations.AlterField(
            model_name='register',
            name='clerk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Atendente'),
        ),
        migrations.AlterField(
            model_name='register',
            name='sent_to',
            field=models.CharField(choices=[('A', 'ENCAMINHADO PARA AGENDAMENTO'), ('F', 'ENCAMINHADO PARA FECHAMENTO'), ('AF', 'ENCAMINHADO PARA AGUARDANDO FECHAMENTO'), ('AC', 'ENCAMINHADO PARA AGUARDANDO CONTATO')], max_length=255, null=True, verbose_name='Encaminhado para'),
        ),
        migrations.AlterField(
            model_name='register',
            name='type_of_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.typeofrequest', verbose_name='Tipo de solicitação'),
        ),
    ]
