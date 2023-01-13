from django.shortcuts import render,redirect
from .models import Etudiant,Faculte

# Create your views here.

def home (request):
    return render(request,'dashboard.html')

def etudiant(request):
    faculte = Faculte.objects.all()
    etudiants = Etudiant.objects.all()
    
    context = {
      "faculte":faculte,
      "etudiants":etudiants,
    }
    
    return render(request,'etudiant.html',context)

def nouveauetudiant(request):
    if request.method =='POST':
        nom = request.POST['nom']
        postnom = request.POST['postnom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        faculte_id = request.POST['faculte']

        new_etudiant = Etudiant(nom=nom, postnom=postnom, prenom=prenom, telephone=telephone, faculte_id=faculte_id)
        
        try:
                new_etudiant.save()
                return redirect('/etudiant')
        except:
                pass

    else:
        faculte = Faculte.objects.all()
    
        
        context = {
        "faculte":faculte,
        
        }
        return render(request,'nouveauEtudiant.html',context)

def supprimeretudiand(request, id):
    etudiant = Etudiant.objects.get(id=id)
    etudiant.delete()
    return redirect('/etudiant')

def editer_etudiant(request,id):
    etudiant = Etudiant.objects.get(id=id)
    faculte = Faculte.objects.all()
 
    
    context = {
      "faculte":faculte,
      "etudiant":etudiant,
    }
    
    return render(request,'edit.html',context)


def modifieretudiant(request,id):
    etudiant = Etudiant.objects.get(id=id)
    if request.method =='POST':
        id= request.POST['idetud']
        nom = request.POST['nom']
        postnom = request.POST['postnom']
        prenom = request.POST['prenom']
        telephone = request.POST['telephone']
        faculte_id = request.POST['faculte']

        modif_etudiant = Etudiant(id=id,nom=nom, postnom=postnom, prenom=prenom, telephone=telephone, faculte_id=faculte_id)
        
        try:
                modif_etudiant.save()
                return redirect('/etudiant')
        except:
                pass

    else:
        faculte = Faculte.objects.all()
    
        
        context = {
        "faculte":faculte,
        
        }
        return render(request,'edit.html',context)
    
