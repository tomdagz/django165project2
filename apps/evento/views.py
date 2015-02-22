from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Evento, Categoria
from apps.users.models import User
from .forms import EventoForm
from django.core.urlresolvers import reverse_lazy

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['eventos'] = Evento.objects.all().order_by('-created')[:6]
        context['categorias'] = Categoria.objects.all()
        return context

class PanelView(TemplateView):

    template_name = 'panel.html'

    def get_context_data(self, **kwargs):
        context = super(PanelView, self).get_context_data(**kwargs)
        context['eventos'] = Evento.objects.filter(organizer__username='admin')
        context['cantidad'] = context['eventos'].count()
        return context

class CrearEvento(CreateView):

    form_class = EventoForm
    template_name = 'crear_evento.html'

    sucess_url = reverse_lazy('evento:panel')

    def form_valid(self, form):
        form.instance.organizer = User.objects.get(pk=1)
        return super(CrearEvento, self).form_valid(form)


class DetalleEvento(DetailView):

    template_name = 'detalle_evento.html'
    model = Evento


class EditarEvento(UpdateView):

    template_name = 'editar_evento.html'
    sucess_url = reverse_lazy('evento:panel')
    model = Evento
    form_class = EventoForm

    def form_valid(self, form):
        form.instance.organizer = User.objects.get(pk=1)
        return super(EditarEvento, self).form_valid(form)

class EliminarEvento(DeleteView):

    template_name = 'eliminar_evento.html'
    model = Evento

    sucess_url = reverse_lazy('evento:panel')
    context_object_name = 'evento'
