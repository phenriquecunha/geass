from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import RegisterCreateForm
from .models import Register, Quiz

#Registro de Atendimento

class RegisterCreateView(CreateView):
    model = Register
    form_class = RegisterCreateForm

    def form_valid(self, form: Register):
        if self.request:
            form.save()

            return redirect('attendance:register_form')
            
        return redirect('attendance:register_form')

class RegisterListView(ListView):
    model = Register

class RegisterDetailView(DetailView):
    model = Register


#NPS
class ControlQualityView(CreateView):

    def formCreateControlQuality(self):
        formCQ = self.request.POST

        Quiz.objects.create(
            name = 'Controle de satisfação do cliente VOANET',
            client = formCQ['client'],
            note = formCQ['note'],
            user = formCQ['user'],
        )





        




