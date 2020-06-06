from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Persona

class PersonaModelForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['name',
                  'characteristics',]
        widgets = {
            'characteristics': CheckboxSelectMultiple(),
        }
