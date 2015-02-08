from django.conf.urls import patterns, include, url
from .views import HomeView, PanelView, CrearEvento, DetalleEvento, EditarEvento, EliminarEvento

urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^panel/$', PanelView.as_view(), name = 'panel'),
    url(r'^panel/evento/nuevo/$', CrearEvento.as_view(), name = 'nuevo'),
    url(r'^panel/evento/(?P<pk>\d+)/$', DetalleEvento.as_view(), name = 'detalle'),
    url(r'^panel/evento/editar/(?P<pk>\d+)/$', EditarEvento.as_view(), name = 'editar'),
    url(r'^panel/evento/eliminar/(?P<pk>\d+)/$', EliminarEvento.as_view(), name = 'eliminar'),

)
