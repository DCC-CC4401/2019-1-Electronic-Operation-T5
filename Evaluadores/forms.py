from django import forms
from Evaluadores.models import *
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib import messages


class AddEvaluador(forms.ModelForm):

    class Meta:
        model = Evaluador
        fields = '__all__'


class UpdateEvaluador(forms.ModelForm):

    ID = forms.CharField(widget=forms.TextInput(attrs={'readonly':'', 'size':'4'}),required=True)
    
    class Meta:
        model = Evaluador
        fields = ['ID','nombre','apellido','correo']

    def save(self, *args, **kwargs):
        # obtener evaluador
        id = int(self.cleaned_data['ID'])
        evaluador = Evaluador.objects.get(pk=id)
        # obtener su perfil de usuario
        username = evaluador.correo
        user = User.objects.get(username=username)

        try:
            # actualizar informacion de usuario
            user.username = self.cleaned_data['correo']
            user.first_name = self.cleaned_data['nombre']
            user.last_name = self.cleaned_data['apellido']
            user.email = self.cleaned_data['correo']
            user.save()
        except IntegrityError:
            return HttpResponseRedirect('..')

        # actualizar informacion database
        evaluador.nombre = user.first_name
        evaluador.apellido = user.last_name
        evaluador.correo  = user.email
        evaluador.update()

        


class AddProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'


