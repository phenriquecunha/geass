from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import DetourCreateForm
from .models import Detour

class DetourCreateView(CreateView):
    model = Detour
    form_class = DetourCreateForm

    def form_valid(self, form: Detour): 
        if self.request:
            form.save()

            return redirect('scheduling:detour_form')
            
        return redirect('scheduling:detour_form')

class DetourListView(ListView):
    model = Detour

class DetourDetailView(DetailView):
    model = Detour

class DetourUpdateView(UpdateView):
    model = Detour
    form_class = DetourCreateForm
    template_name_suffix = '_update_form'


    def form_valid(self, form: Detour): 
        if self.request:
            form.save()

            return redirect('scheduling:detour_list')
            
        return redirect('scheduling:detour_list')

class DetourDeleteView(DeleteView):
    model = Detour
    success_url = reverse_lazy('scheduling:detour_list')


