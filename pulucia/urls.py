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
    path('', include('pwa.urls')),

    path('', views.index_page, name='index_page'),
    path('affiche/<int:pk>', views.affiche, name='affiche'),

    path('librairie/', views.librairie, name='librairie'),
    path('librairie/livre/<int:pk>', views.livre, name='livre'),
    path('librairie/search/<slug:slug>', views.librairie_search, name='librairie-search'),
    path('librairie/achat', views.achat_livre, name='achat-livre'),
    path('store/', views.store, name='store'),


    path('bibliotheque', views.bibliotheque, name='bibliotheque'),
    path('bibliotheque/search/<slug:slug>', views.bibliotheque_search, name='bibliotheque-search'),
    path('reader/<int:pk>', views.reader, name='reader'),
    path('reader1/<int:pk>', views.reader1, name='reader1'),
    path('bibliotheque/add-book/<int:pk>', views.add_book_profile, name='add-book'),
    path('bibliotheque/add-book-categorie/<slug:slug>/<int:pk>', views.add_book_profile_categorie, name='add-book-categorie'),
    
    path('bibliotheque/remove-book/<int:pk>', views.remove_book_profile, name='remove-book'),



    path('evenement/<int:pk>', views.evenement, name='evenement'),
    path('evenement-main-page', views.evenement_main1, name='evenement-main'),
    path('blog', views.blog, name='blog'),
    path('blog/article/<int:pk>', views.article, name='article'),

    path('comment/article/<int:pk>', views.comment_article1, name='comment'),
    path('comment/publication/<int:pk>', views.comment_text1, name='comment-text'),

    path('publication', views.publication1, name='publication'),
    path('publication/text/<int:pk>', views.text1, name='text1'),
    path('publication/search/<slug:slug>', views.publication_search_categorie, name='publication-search'),
    path('publication/search-theme/<slug:slug>', views.publication_search_theme, name='publication-search-theme'),


    path('projet', views.projet_main, name='projet'),
    path('projet/projet-details/<int:pk>', views.projet_details, name='projet-details'),
    path('projet/don', views.don1, name='don-projet'),

    path('login', views.login_profile, name='login'),
    path('redirect/', views.redirect_social, name='redirect'),
    path('logout', views.logout_page, name='logout'),
    path('inscrire', views.inscrire, name='inscrire'),

    path('profile/', views.profile, name='profile'),

    path('like/<int:pk>', views.like_post, name="like_post"),
    path('publication/like/<int:pk>', views.like_text, name="like_text"),

    path('article/share/<int:pk>', views.share_article, name="share-article"),
    path('publication/share/<int:pk>', views.share_text, name="share-text"),

    path('videos', views.videos, name='videos'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('temoignages/', views.temoignages, name='temoignages'),
    path('a-propos/', views.a_propos, name='a_propos'),

    path('email/', views.email_info1, name='email-info'),

    path('legal/', views.confidentialite, name='confidentialite'),

    
    path('admin/', admin.site.urls),

    #reset password=======================================================
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="reset-password.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="email-password-sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password-reset-confirm.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password-reset-complete.html"), 
        name="password_reset_complete"),
    
]


#upload image from database
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) # solve the issue the css doesn't affect the page



