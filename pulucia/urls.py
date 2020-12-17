"""pulucia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from pulucia_web import views
from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('librairie/', views.librairie, name='librairie'),
    path('librairie/livre', views.livre, name='livre'),
    path('bibliotheque', views.bibliotheque, name='bibliotheque'),
    path('reader', views.reader, name='reader'),
    path('evenement', views.evenement, name='evenement'),
    path('evenement-main-page', views.evenement_main, name='evenement-main'),
    path('blog', views.blog, name='blog'),
    path('blog/article', views.article, name='article'),
    path('publication', views.publication, name='publication'),
    path('publication/text', views.text, name='text'),
    path('projet', views.projet, name='projet'),
    path('projet/projet-details', views.projet_details, name='projet-details'),
    path('login', views.login, name='login'),
    path('inscrire', views.inscrire, name='inscrire'),


    path('temoignages/', views.temoignages, name='temoignages'),
     path('a-propos/', views.a_propos, name='a_propos'),
    path('admin/', admin.site.urls),
    
]


#upload image from database
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
