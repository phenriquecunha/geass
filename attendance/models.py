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
        ("AG" ,"AGENDAMENTO"),
        ("F", "FECHAMENTO"),
        ("AF", "AGUARDANDO FECHAMENTO"),
        ("AC","AGUARDANDO CONTATO"),
        ("EA", "EM ANALISE"),
    )

    SENT_FROM_CHOICES = (
        ("AN", "ANDAMENTO"),
        ("AC", "AGUARDANDO CONTATO"),
        ("AF", "AGUARDADO FECHAMENTO"),
        ("EA", "EM ANALISE"),
        ("CH","CHAT")
    )

    date = models.DateField(verbose_name='Data de registro',  auto_now_add=True)
    protocol = models.IntegerField(verbose_name='Protocolo de atendimento', primary_key=True)
    type_of_request = models.ForeignKey(TypeOfRequest, verbose_name="Tipo de solicitação", on_delete=CASCADE)
    sent_from = models.CharField(verbose_name="Encaminhado de", max_length=255, choices=SENT_FROM_CHOICES, null=True)
    sent_to = models.CharField(verbose_name="Encaminhado para", max_length=255, choices=SENT_TO_CHOICES, null=True)
    clerk = models.ForeignKey(User, verbose_name="Atendente", on_delete=CASCADE)

    def __str__(self):
        return str(self.protocol)

class Service(TimeStampedModel):
    nameFlat = models.CharField('Nome do plano', max_length=255)
    infrastructure = models.CharField('Infraestrutura', max_length=255)
    user = models.ForeignKey(User, on_delete=CASCADE)

class Client(TimeStampedModel):
    name = models.CharField('Nome', max_length=255)
    city = models.CharField('Cidade', max_length=255)
    district = models.CharField('Bairro', max_length=255)
    street = models.CharField('Rua', max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    service = models.ForeignKey(Service, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

class Question(TimeStampedModel):
    name = models.CharField('Nome', max_length=255)
    answer = models.CharField('Resposta', max_length=255)


class Quiz(TimeStampedModel):
    name = models.CharField('Nome', max_length=255)
    client = models.ForeignKey(Client, on_delete=CASCADE)
    questions = models.ForeignKey(Question, on_delete=CASCADE)
    note = models.TextField('Observação')





