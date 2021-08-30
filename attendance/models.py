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

    date = models.DateField(verbose_name='Data de registro',  auto_now_add=True)
    protocol = models.IntegerField(verbose_name='Protocolo de atendimento', primary_key=True)
    type_of_request = models.ForeignKey(TypeOfRequest, on_delete=CASCADE)
    sent_to = models.CharField(max_length=255, choices=SENT_TO_CHOICES)
    clerk = models.ForeignKey(User, on_delete=CASCADE)