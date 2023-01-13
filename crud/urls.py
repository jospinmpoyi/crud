 
from django.urls import path 
from .import views

urlpatterns = [
     
    path('',views.home,name="dashboard"),
    path('etudiant',views.etudiant,name="etudiant"),
    path('nouveauetudiant',views.nouveauetudiant,name="nouveauetudiant"),
    path('supprimer/<int:id>',views.supprimeretudiand,name="supprimeretudiand"),
    path('edit/<int:id>',views.editer_etudiant,name="editer_etudiant"),
    path('modifier/<int:id>',views.modifieretudiant,name="modifieretudiant"),
]
