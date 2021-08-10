from django.db import models
from django.db.models.deletion import CASCADE
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
    score = models.FloatField("Pontuação", default=0)
    team = ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class TypeOfRequest(TimeStampedModel):
    name = models.CharField("Nome", max_length=255)
    weight = models.FloatField("Peso", default=1)

    def __str__(self):
        return f'{self.name}'

class DailyMonitoring(TimeStampedModel):
    date = models.DateField("Data")
    current_balance = models.IntegerField("Saldo Atual")
    open = models.IntegerField("Abertas")
    completed = models.IntegerField("Concluídas")
    previous_balance = models.IntegerField("Saldo Anterior")
    type_of_request = models.ForeignKey(TypeOfRequest, verbose_name="Tipo de solcitiação", on_delete=CASCADE)

    def __str__(self):
        return f'{self.date}'

class Detour(TimeStampedModel):
    date = models.DateField("Data")
    installations = models.IntegerField("Instalações")
    detour = models.IntegerField("Desvio", null=True)
    calculation_basis = models.IntegerField("Base do calculo", default=5)
    justification = models.TextField("Justificativa")
    technical = models.ManyToManyField(Technician, verbose_name="Técnicos")

    def __str__(self):
        return ' e '.join([t.name for t in self.technical.all()])
    
    def get_technical(self):
        return ' e '.join([t.name for t in self.technical.all()])
    
    def get_absolute_url_for_detail(self):
        return reverse('scheduling:detour_detail', kwargs={'pk': self.id})

    def get_absolute_url_for_update(self):
        return reverse('scheduling:detour_update', kwargs={'pk': self.id})

    def get_absolute_url_for_delete(self):
        return reverse('scheduling:detour_list', kwargs={'pk': self.id})

class AttachmentsDetour(models.Model):
    detour = models.ForeignKey(
        Detour, 
        on_delete=models.CASCADE, 
        null=True, 
        verbose_name='anexos',
        related_name='images'
    )
    image = models.ImageField(null=False, blank=False, upload_to='%Y/%m/%d')

    def __str__(self):
        return str(self.detour)
        
class Request(TimeStampedModel):
    protocol = models.IntegerField(primary_key=True),
    local = models.CharField("Localidade", max_length=255)
    status = models.BooleanField("Status")
    note = models.TextField("Observação")
    r_factor = models.IntegerField("Fator R")
    type_of_request = models.ForeignKey(TypeOfRequest, verbose_name="Tipo de solcitiação", on_delete=CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.protocol}'


def calculateDetour(sender, instance, created, **kwargs):
        Detour.objects.filter(id = instance.id).update(detour = (instance.calculation_basis - instance.installations))

post_save.connect(calculateDetour, sender=Detour)