from django.db import models
from django import forms
from django.contrib.auth.models import User
import numpy as np
import random



# Create your models here.
sexe_choices=(("Homme","Homme"), ("Femme", "Femme"))

pays_residence_choices=(("Haiti","Haiti"),("France","France"),("Canada","Canada"),("USA","USA"),
("R Domninicaine","R Dominicaine"),("Chilie","Chilie"),("Guyanne","Guyanne"),("Martinique","Martinique"),
("Guadeloupe","Guadeloupe"),("Espagne","Espagne"),("Angleterre","Angleterre"),("Autre","Autre"))

class inscription(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sexe=models.CharField(max_length=45, choices=sexe_choices,  blank=False)
    pays_residence=models.CharField(max_length=45, choices=pays_residence_choices,  blank=False, verbose_name="Pays de residence")
    telephone=models.CharField(max_length=45, unique=True,  blank=True)
    def __str__(self):
        return self.user.username

class librairie_categorie(models.Model):
    categorie=models.SlugField(max_length=45, blank=False, unique=True)
    def __str__(self):
        return self.categorie

class livre_librairie(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    code_livre=models.CharField(max_length=45,  blank=False, unique=True)
    titre_du_livre=models.CharField(max_length=45,   blank=False)
    categorie=models.ForeignKey(librairie_categorie, on_delete=models.CASCADE, blank=False)
    auteur=models.CharField(max_length=45,  blank=False)
    a_propos_du_livre=models.TextField(max_length=8000, blank=False)
    a_propos_de_auteur=models.TextField(max_length=8000, blank=False)
    annee=models.IntegerField(blank=False)
    page=models.IntegerField(blank=False)
    cover_image=models.ImageField(upload_to="librairie",  blank=False)
    document=models.FileField(upload_to="librairie", blank=True)
    prix=models.PositiveIntegerField(default=0)
    book_add=models.ManyToManyField(User, blank=True, related_name='book_add2')
    def __str__(self):
        return self.titre_du_livre

class point_vente_livre(models.Model):
    code_livre = models.ForeignKey(livre_librairie, related_name='livre', on_delete=models.CASCADE)
    local=models.CharField(max_length=45,  blank=False)
    commune=models.CharField(max_length=45,  blank=False)
    adresse=models.CharField(max_length=45,  blank=False)
    telephone=models.CharField(max_length=45,  blank=False)
    email=models.EmailField(blank=False)
    def __str__(self):
        return self.code_livre.titre_du_livre

class blog_pulucia(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    titre=models.CharField(max_length=300,   blank=False)
    redacteur=models.CharField(max_length=45,  blank=False)
    categorie=models.CharField(max_length=45,  blank=False)
    text=models.TextField(max_length=30000, blank=False)
    image=models.ImageField(upload_to="blog",  blank=False)
    image_source=models.CharField(max_length=300,   blank=False)
    views = models.PositiveIntegerField(default=0)
    share = models.PositiveIntegerField(default=0)
    likes=models.ManyToManyField(User, blank=True, related_name='likes')
    
    def total_likes(self):
        return self.likes.count() 
    

    def __str__(self):
        return self.titre


class comment_article(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    article=models.ForeignKey(blog_pulucia, on_delete=models.CASCADE, blank=False)
    comment = models.TextField(max_length=3000, blank=False, verbose_name="Poster  un commentaire")
    def total_comment(self):
        return self.comment.count() 

class evenement_main(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    titre=titre=models.CharField(max_length=300,   blank=False)
    description=models.TextField(max_length=1000, blank=False)
    image_cover=models.ImageField(upload_to="evenement",  blank=False)
    def __str__(self):
        return self.titre

class evenement_photo(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    evenement=models.ForeignKey(evenement_main, on_delete=models.CASCADE, blank=False)
    photo=models.ImageField(upload_to="evenement",  blank=False)
    note_photo=models.CharField(max_length=100,  blank=True)


class publication_auteur(models.Model):
    auteur=models.CharField(max_length=45, blank=False, unique=True)
    def __str__(self):
        return self.auteur



    

class publication_theme(models.Model):
    theme=models.CharField(max_length=45, blank=False, unique=True)
    def __str__(self):
        return self.theme

        
categorie_choices=(("Poesies","Poesies"), ("Contes-et-Legendes", "Contes-et-Legendes"), ("Nouvelles", "Nouvelles"))
class publication(models.Model):
    def color():
        color = list(np.random.choice(range(256), size=3))
        color_pub= color
        return tuple(color_pub)
    date=models.DateTimeField(auto_now_add=True)
    auteur=models.ForeignKey(publication_auteur, on_delete=models.CASCADE, blank=False)
    theme=models.ForeignKey(publication_theme, on_delete=models.CASCADE, blank=False)
    categorie=models.SlugField(max_length=45, choices=categorie_choices,  blank=False, default='poesie')
    titre=titre=models.CharField(max_length=300,   blank=False)
    poeme=models.TextField(max_length=4000, blank=True)
    text=models.TextField(max_length=20000, blank=True)
    couleur=models.CharField( max_length=45, default=color)
    views1 = models.PositiveIntegerField(default=0)
    likes1=models.ManyToManyField(User, blank=True, related_name='likes1')
    share1 = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.titre

    def total_likes(self):
        return self.likes1.count() 
    
    def get_comment_count(self):
        return comment_text2.objects.filter(text__titre=self).count()


class comment_text2(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    text=models.ForeignKey(publication, on_delete=models.CASCADE, blank=False)
    comment=models.TextField(max_length=3000, blank=False)
    def total_comment(self):
        return self.comment.count() 

class video_youtube(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    titre=titre=models.CharField(max_length=90,   blank=False)
    link=models.CharField(max_length=90,   blank=False)
    note=models.CharField(max_length=200,   blank=False)
    def __str__(self):
        return self.titre


class projet(models.Model):
     date=models.DateTimeField(auto_now_add=True)
     titre=models.CharField(max_length=90,   blank=False)
     description=models.TextField(max_length=3000, blank=False)
     objectif=models.TextField(max_length=500, blank=False)
     cible=models.TextField(max_length=400, blank=False)
     resultats=models.TextField(max_length=1000, blank=False)
     phase=models.TextField(max_length=1000, blank=False)
     budget=models.TextField(max_length=1000, blank=False)
     partenaire=models.TextField(max_length=400, blank=False)
     cover_img=models.ImageField(upload_to="projet",  blank=False)
     def __str__(self):
        return self.titre


class bibliotheque_domaine(models.Model):
    categorie=models.SlugField(max_length=45, blank=False, unique=True)
    def __str__(self):
        return self.categorie

class bibliotheque1(models.Model):
     date=models.DateTimeField(auto_now_add=True)
     titre=models.CharField(max_length=400,   blank=False)
     auteur=models.CharField(max_length=90, blank=False)
     categorie=models.ForeignKey(bibliotheque_domaine, on_delete=models.CASCADE, blank=False)
     document=models.FileField(upload_to="bibliotheque", blank=False)
     image_cover=models.ImageField(upload_to="bibliotheque", blank=False)
     book_add=models.ManyToManyField(User, blank=True, related_name='book_add1')
     
     def __str__(self):
        return self.titre


class carousel_image(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    titre=models.CharField(max_length=100,   blank=False)
    image=models.ImageField(upload_to="carousel", blank=False)
    def __str__(self):
        return self.titre

class affiche1(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    titre=models.CharField(max_length=100,   blank=False)
    message=models.TextField(max_length=500,   blank=True)
    image=models.ImageField(upload_to="carousel", blank=False)
    def __str__(self):
        return self.titre


class don(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    projet=models.CharField(max_length=400,   blank=False)
    nom=models.CharField(max_length=100,   blank=True)
    email=models.EmailField(blank=True)
    montant=models.CharField(max_length=100,   blank=False)
    def __str__(self):
        return self.projet
class livre_achat(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    user=models.CharField(max_length=400,   blank=False)
    email=models.EmailField(blank=True)
    titre=models.CharField(max_length=400,   blank=False)
    montant=models.CharField(max_length=100,   blank=False)
    def __str__(self):
        return self.titre

class email_info(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    email=models.EmailField()
    def __str__(self):
        return self.email

class store_amazon(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    products=models.TextField(max_length=6000, blank=False)
    def __str__(self):
        return self.products















    


    













