from django.views.generic import CreateView, FormView, ListView
from django.urls import reverse_lazy

from .models import Characteristic, Persona
from .forms import PersonaModelForm

class HomeView(ListView):
    template_name = 'persona/home.html'
    model = Persona
    context_object_name = 'personas'


class CharacteristicCreateView(CreateView):
    model = Characteristic
    template_name = 'persona/add_characteristic.html'
    fields = ['name',]
    success_url = reverse_lazy('persona:add_characteristic')


class PersonaAddFormView(FormView):
    form_class = PersonaModelForm
    template_name = 'persona/add_persona.html'
    success_url = reverse_lazy('persona:add_persona')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
