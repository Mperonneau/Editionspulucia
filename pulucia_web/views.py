from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
#from .forms import *
#from .filters import *
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from .decorators import *
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from random import randint
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.

def index_page(request):
    return render(request, 'index.html')

def librairie(request):
    return render(request, 'librairie_main.html')

def livre(request):
    return render(request, 'livre.html')

def bibliotheque(request):
    return render(request, 'bibliotheque.html')

def reader(request):
    return render(request, 'reader.html')


def evenement(request):
    return render(request, 'evenement.html')

def evenement_main(request):
    return render(request, 'evenement_main.html')

def article(request):
    return render(request, 'article.html')

def blog(request):
    return render(request, 'blog.html')

def publication(request):
    return render(request, 'publication.html')

def text(request):
    return render(request, 'text.html')

def temoignages(request):
    return render(request, 'temoignages.html')

def a_propos(request):
    return render(request, 'a-propos.html')

def projet(request):
    return render(request, 'projet.html')

def projet_details(request):
    return render(request, 'projet-details.html')

def login(request):
    return render(request, 'login.html')

def inscrire(request):
    return render(request, 'inscrire.html')