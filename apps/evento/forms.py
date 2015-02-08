from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        exclude = ('views', 'created', 'modified',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'sumary': forms.Textarea(attrs={'class': 'form-control', 'rows': '2' }),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '2' }),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'start': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'finish': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_free': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),

        }
