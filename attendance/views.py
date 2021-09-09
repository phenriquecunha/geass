from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from .forms import RegisterCreateForm, QuizCreateForm
from .models import Register, Quiz, Client, Question

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
    model = Quiz
    form_class = QuizCreateForm

    def form_valid(self, form: Quiz):
        formPost = self.request.POST
        user = self.request.user

        if self.request:
            quiz = form.save(commit=False)
            quiz.name = 'Questionario de qualidade do serviço'
            quiz.user = user
            quiz.save()

            Question.objects.create(
                name = 'De 0 a 10 . . .',
                answer = formPost['answer_1'],
                quiz = quiz,
                user = user
            )

            Question.objects.create(
                name = 'De 0 a 15 . . .',
                answer = formPost['answer_2'],
                quiz = quiz,
                user = user
            )

            Question.objects.create(
                name = 'De 0 a 20 . . .',
                answer = formPost['answer_3'],
                quiz = quiz,
                user = user
            )


            return redirect('attendance:quiz_form')

        return redirect('attendance:quiz_form')
            





        




