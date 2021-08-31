from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel

from scheduling.models import TypeOfRequest

from django.conf import settings
User = settings.AUTH_USER_MODEL

class Register(TimeStampedModel):
    SENT_TO_CHOICES = (
        ("A", "ENCAMINHADO PARA AGENDAMENTO"),
        ("F", "ENCAMINHADO PARA FECHAMENTO"),
        ("AF", "ENCAMINHADO PARA AGUARDANDO FECHAMENTO"),
        ("AC", "ENCAMINHADO PARA AGUARDANDO CONTATO"),
    )

    SENT_FROM_CHOICES = (
        ("A", "ANDAMENTO"),
        ("AC", "AGUARDANDO CONTATO"),
        ("AF", "AGUARDADO FECHAMENTO"),
        ("EA", "EM ANALISE"),
        ("CH", "CHAT")
    )

    date = models.DateField(verbose_name='Data de registro',  auto_now_add=True)
    protocol = models.IntegerField(verbose_name='Protocolo de atendimento', primary_key=True)
    type_of_request = models.ForeignKey(TypeOfRequest, verbose_name="Tipo de solicitação", on_delete=CASCADE)
    sent_from = models.CharField(verbose_name="Encaminhado de", max_length=255, choices=SENT_FROM_CHOICES, null=True)
    sent_to = models.CharField(verbose_name="Encaminhado para", max_length=255, choices=SENT_TO_CHOICES, null=True)
    clerk = models.ForeignKey(User, verbose_name="Atendente", on_delete=CASCADE)

    def __str__(self):
        return str(self.protocol)