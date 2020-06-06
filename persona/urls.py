from django.urls import path

from .views import HomeView, CharacteristicCreateView, PersonaAddFormView

app_name = 'persona'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/characteristic/', CharacteristicCreateView.as_view(),
    name='add_characteristic'),
    path('add/persona/', PersonaAddFormView.as_view(),
    name='add_persona'),
]
