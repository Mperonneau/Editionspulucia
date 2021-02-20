from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

class CreateUserMembre(UserCreationForm):
    username=forms.CharField(max_length=45, label="Nom d'utilisateur")
    email=forms.EmailField(required=True, label="Adresse electornique")
    first_name=forms.CharField(max_length=45, required=True, label="Prénom")
    last_name=forms.CharField(max_length=45, required=True, label="Nom")
    
    def __init__(self, *args, **kwargs): # prevent to cursor to go directly to field username.
            super(CreateUserMembre, self).__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.pop("autofocus", None)
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email','username', 'password1','password2']

    
    def clean(self):
       username=self.cleaned_data.get('username')
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
           msg="Cet email est dejà associé à un compte"
           self.add_error('email',msg) #to associate the error message to a specific field

       if User.objects.filter(username=username).exists():
            msg="Ce username existe dejà."
            self.add_error('username',msg) #to associate the error message to a specific field
       return self.cleaned_data

   # def clean_email(self):
       # email= self.cleaned_data.get("email")
       # if email !="":
           # return email
       # else:
           # raise forms.ValidationError("Ce champ est obligatoire")

class inscriptionform(forms.ModelForm):
    class Meta:
        model = inscription
        exclude = ['date','user']

    def clean_telephone(self):
            telephone= self.cleaned_data.get("telephone")
            if telephone.isdigit()==True or telephone=='':
                return telephone
            else:
                     raise forms.ValidationError("Le numero de telephone n'est pas valide")



class comment_article_form(forms.ModelForm):
    class Meta:
        model = comment_article
        exclude = ['date','user','article']

class comment_text_form(forms.ModelForm):
    class Meta:
        model = comment_text2
        exclude = ['date','user','text']

class email_form(forms.ModelForm):
    class Meta:
        model=email_info
        fields="__all__"
        

    

