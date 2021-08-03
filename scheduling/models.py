from django.db import models
from django.db.models.fields import BigIntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from model_utils.models import TimeStampedModel

from django.urls import reverse

class Team(TimeStampedModel):
    name = models.CharField("Nome", max_length=255)
    service = models.CharField("Serviço que realiza", max_length=255)

    def __str__(self):
        return f'{self.name}'

class Technician(TimeStampedModel):
    name = models.CharField("Nome", max_length=255)
    telephone = models.CharField("Telefone", max_length=255)
    team = ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Detour(TimeStampedModel):
    date = models.DateField("Data")
    installations = models.IntegerField("Instalações")
    detour = models.IntegerField("Desvio", null=True)
    justification = models.TextField("Justificativa")
    technical = models.ManyToManyField(Technician, verbose_name="Técnicos")

    def __str__(self):
        return '\n'.join([t.name for t in self.technical.all()])
    
    def get_technical(self):
        return '\n'.join([t.name for t in self.technical.all()])
    
    def get_absolute_url_for_detail(self):
        return reverse('scheduling:detour_detail', kwargs={'pk': self.id})

    def get_absolute_url_for_update(self):
        return reverse('scheduling:detour_update', kwargs={'pk': self.id})

    def get_absolute_url_for_delete(self):
        return reverse('scheduling:detour_list', kwargs={'pk': self.id})
    
        

class Request(TimeStampedModel):
    protocol = models.IntegerField(primary_key=True),
    type = models.CharField("Tipo de solicitação", max_length=10)
    local = models.CharField("Localidade", max_length=255)
    status = models.BooleanField("Status")
    note = models.TextField("Observação")
    r_factor = models.IntegerField("Fator R")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.protocol}'


def calculateDetour(sender, instance, created, **kwargs):
        Detour.objects.filter(id = instance.id).update(detour = (5 - instance.installations))

post_save.connect(calculateDetour, sender=Detour)