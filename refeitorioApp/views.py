from django.shortcuts import render
from refeitorioApp.forms import Alunoforms
from refeitorioApp.

# Create your views here.
def home(request):
    aluno = aluno.objects.all()
    form =Alunoforms()
    context ={'form':form}
     return render(request,'refeitorio/home.html' ,context)


def new_aluno(request):
     form= Alunoforms(request.POST, request.FILES)
    if request.method == "POST" :
    #form =Alunoforms(request.post,request.FILES)
    if form.is_valid():
     aluno=form.save()
     aluno.save()
    form={'form'}
 context={'form':form 'aluno':alunos}
    return render (request,'refeitorio/home.html', context ),

def mostrar_aluno(request):
    aluno =aluno.objects.all() #todos os objetos que estiverem na classe do aluno
    context={'alunos':aluno}
    return render(request,'refeitorio/new_aluno.html',context)


   def editar_aluno (request,id):
    aluno =get_object_or_404(Aluno, pk=id)
    form= Alunoforma