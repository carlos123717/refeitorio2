from dataclasses import fields

from refeitorioApp.models import Aluno, Evento
from django import forms

class Alunoforms(forms.ModelForm):
 class Meta:
     model= Aluno
     fields ['nome_aluno''matricula_aluno''foto_aluno']
     #fields="___all___"

class AlunoEvento(forms.ModelForm)
 class meta:

         evento=Aluno