from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
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
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Module to send email when there is a new record 
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver # for signal django (trigger multiple events)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail





# Create your views here.

@receiver(post_save, sender=publication_auteur) 
def email(sender,  instance, created, **kwargs): 
    #subject = 'Nouveau Article'
    #message =instance.auteur 
    #email_from = settings.EMAIL_HOST_USER
    #recipient_list = ['peronneaumoliere@gmail.com',]
    #send_mail( subject, message, email_from, recipient_list )
    #subject, from_email, to = 'Nouveau Article', 'peronneaumoliere@gmail.com', 'peronneaumoliere@gmail.com'
    #text_content = 'This is an important message.'
   # html_content = '<p>This is an <strong>important</strong> message.' + instance.auteur + '</p>'
    #msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
   # msg.attach_alternative(html_content, "text/html")
   # msg.send()

#the html method
    #subject, from_email, to = 'Subject', 'from@xxx.com', 'to@xxx.com'
    #subject, from_email, to = 'Nouveau Article', 'peronneaumoliere@gmail.com', 'peronneaumoliere@gmail.com'
    #html_content = render_to_string('temoignages.html') # render with dynamic value
    #text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

# create the email, and attach the HTML version as well.
   # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #msg.attach_alternative(html_content, "text/html")
   # msg.send()

    send_mail('Subject here', 'Here is the message.', 'peronneaumoliere@gmail.com', ['peronneaumoliere@gmail.com'])



def index_page(request):
    carousel=carousel_image.objects.all().order_by('-date')[:5]
    blog1=blog_pulucia.objects.all().order_by('-date')[:3]
    affiche=affiche1.objects.all().order_by('-date')[:3]
    evenement=evenement_main.objects.all().order_by('-date')[:4]
    context={
        'carousel':carousel,
        'blog1':blog1,
        'affiche':affiche,
        'evenement':evenement,

    }
    return render(request, 'index.html', context)

def affiche(request, pk):
    affiche=affiche1.objects.get(pk=pk)
    #affiche=affiche1.objects.all().order_by('-date')[:3]
    context={
        #'affiche2':affiche2,
        'affiche':affiche,

     }

    if request.is_ajax():
            html= render_to_string('message_affiche.html', context, request=request)
            return JsonResponse({'form':html})
    return redirect('index_page')



def login_profile(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next1=request.POST.get('next') #to get the previous url 
           
            if next1:
                return HttpResponseRedirect(next1) # redirect to the previous page after login
            else:
                return redirect('profile') 
        else:
            messages.info(request, "Le Username ou le Password est incorrect")      
    context = {}
    return render (request, 'login.html' , context)

def redirect_social(request):
    if 'next' in request.GET:
            return HttpResponseRedirect(request.GET['next'])
    else:
     return redirect('index_page')
     
   

def logout_page(request): #member and volunteer
    logout(request)
    return redirect('index_page')

def inscrire(request):
    form_user=CreateUserMembre()
    form=inscriptionform()
    if request.method == 'POST':
        form_user=CreateUserMembre(request.POST)
        form=inscriptionform(request.POST)
        if form.is_valid() and form_user.is_valid():
              user = form_user.save()
              form=form.save(commit=False)
              form.user=user
              form.save()
              messages.success(request, f"Votre compte a été crée avec succes!")
              return redirect('login')
    context={
        'form_user':form_user,
        'form':form
    }
    return render(request, 'inscrire.html', context)


def librairie(request):
    livre=livre_librairie.objects.all().order_by('-date')
    categorie1=livre_librairie.objects.all().order_by('-date')
    livre_search=librairiefilter(request.GET, queryset=livre)
    paginator=Paginator(livre_search.qs, 19)
    page=request.GET.get('page')

    try:
        livre1= paginator.page(page)
    except PageNotAnInteger:
        livre1 = paginator.page(1)
    except EmptyPage:
        livre1 = paginator.page(paginator.num_pages)
    #auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)

    list1=[]
    for a in categorie1:
        list1.append(a.categorie)
    
    categorie=[]
    for x in list1:
        if x not in categorie:
            categorie.append(x)

    context={
        'livre':livre1,
        'livre_search':livre_search,
        'categorie':categorie,
    }
    return render(request, 'librairie_main.html', context)


def librairie_search(request, slug):
    livre=livre_librairie.objects.filter(categorie__categorie=slug).order_by('-date')
    categorie1=livre_librairie.objects.all().order_by('-date')
    livre_search=librairiefilter(request.GET, queryset=livre)
    paginator=Paginator(livre_search.qs, 19)
    page=request.GET.get('page')

    try:
        livre1= paginator.page(page)
    except PageNotAnInteger:
        livre1 = paginator.page(1)
    except EmptyPage:
        livre1 = paginator.page(paginator.num_pages)
    #auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)

    list1=[]
    for a in categorie1:
        list1.append(a.categorie)
    
    categorie=[]
    for x in list1:
        if x not in categorie:
            categorie.append(x)

    context={
        'livre':livre1,
        'livre_search':livre_search,
        'categorie':categorie,
    }
    return render(request, 'librairie_main.html', context)



def livre(request, pk):
    livre=livre_librairie.objects.get(pk=pk)
    pt_vente=point_vente_livre.objects.filter( code_livre__code_livre=livre.code_livre)
    
    context={
        'livre':livre,
        'pt_vente':pt_vente,
    }
    return render(request, 'livre.html', context)


def bibliotheque(request):
    livre=bibliotheque1.objects.all().order_by('-date')
    categorie1=bibliotheque1.objects.all()
    livre_search= bibliothequefilter(request.GET, queryset=livre)
    paginator=Paginator(livre_search.qs, 19)
    page=request.GET.get('page')
   
    try:
        livre1= paginator.page(page)
    except PageNotAnInteger:
        livre1 = paginator.page(1)
    except EmptyPage:
        livre1 = paginator.page(paginator.num_pages)

    list1=[]
    for a in categorie1:
        list1.append(a.categorie)
    
    categorie=[]
    for x in list1:
        if x not in categorie:
            categorie.append(x)

    context={
        'livre':livre1,
        'categorie':categorie,
        'livre_search':livre_search,
    }
    return render(request, 'bibliotheque.html', context)

def bibliotheque_search(request , slug):
    livre=bibliotheque1.objects.filter(categorie__categorie=slug).order_by('-date')
    categorie1=bibliotheque1.objects.all()
    livre_search= bibliothequefilter(request.GET, queryset=livre)
    paginator=Paginator(livre_search.qs, 19)
    page=request.GET.get('page')
    theme_par=slug
   
    try:
        livre1= paginator.page(page)
    except PageNotAnInteger:
        livre1 = paginator.page(1)
    except EmptyPage:
        livre1 = paginator.page(paginator.num_pages)

    list1=[]
    for a in categorie1:
        list1.append(a.categorie)
    
    categorie=[]
    for x in list1:
        if x not in categorie:
            categorie.append(x)

    context={
        'livre':livre1,
        'categorie':categorie,
        'livre_search':livre_search,
        'theme_par':theme_par,
    }
    return render(request, 'bibliotheque.html', context)


@login_required
def add_book_profile(request, pk):
    if request.user.is_authenticated:
        data = dict()
        livre=bibliotheque1.objects.all().order_by('-date')
        book=get_object_or_404(bibliotheque1, pk=pk) 
        is_add=False
        if book.book_add.filter(id=request.user.id).exists():
            book.book_add.remove(request.user)
            is_add=False
        else:
            book.book_add.add(request.user)
            is_liked=True

        context={
            'book':book,
            'livre':livre,  
        }
        

        if request.is_ajax():
            html= render_to_string('add_book_t.html', context, request=request)
            return JsonResponse({'form':html})
    return redirect('bibliothque')

@login_required
def add_book_profile_categorie(request, slug, pk):
    if request.user.is_authenticated:
        data = dict()
        livre=bibliotheque1.objects.filter(categorie__categorie=slug).order_by('-date')
        book=get_object_or_404(bibliotheque1, pk=pk) 
        theme_par=slug
        is_add=False
        if book.book_add.filter(id=request.user.id).exists():
            book.book_add.remove(request.user)
            is_add=False
        else:
            book.book_add.add(request.user)
            is_liked=True

        context={
            'book':book,
            'livre':livre, 
            'theme_par':theme_par, 
        }
        
        if request.is_ajax():
            html= render_to_string('add_book_t.html', context, request=request)
            return JsonResponse({'form':html})
    return redirect('bibliothque')


@login_required
def remove_book_profile(request, pk):
    book=get_object_or_404(bibliotheque1, pk=pk) 
    book.book_add.remove(request.user) 
    return redirect('profile')

@login_required
def profile(request):
    book=bibliotheque1.objects.filter(book_add__username=request.user)

    context={
            'book':book,
            
        }
    return render(request, 'profile.html', context)

def reader(request, pk):
    livre=bibliotheque1.objects.get(pk=pk)
    context={
        'livre':livre,
    }
    return render(request, 'reader_bon.html', context)



    
 




def evenement(request, pk):
    evenement=evenement_main.objects.get(pk=pk)
    evenement_photo1=evenement_photo.objects.filter(evenement__pk=evenement.pk)
    context={
        'evenement':evenement,
        'evenement_photo': evenement_photo1
    }
    return render(request, 'evenement1.html', context)


def evenement_main1(request):
    evenement=evenement_main.objects.all().order_by('-date')
    context={
        'evenement':evenement,
    }
    return render(request, 'evenement_main.html', context)


def article(request, pk):
    article=blog_pulucia.objects.get(pk=pk)
    recent=blog_pulucia.objects.all().order_by('-date')[:5]
    plus_lus=blog_pulucia.objects.all().order_by('-views')[:5]
    top=blog_pulucia.objects.all().order_by('-views')[:1]
    commentaire=comment_article.objects.filter(article__pk=article.pk).order_by('-date')
    total_comment=commentaire.count()
    form=comment_article_form()
    article.views+=1
    article.save()
    context={
        'article':article,
        'recent':recent,
        'plus_lus':plus_lus,
        'top':top,
        'total_likes':article.total_likes(),
        'commentaire':commentaire,
        'total_comment':total_comment,
        'form':form,
       
    }
    return render(request, 'article.html', context)

def share_article(request, pk):
    article=blog_pulucia.objects.get(pk=pk)
    article.share+=1
    article.save()
    context={
        'article':article,
    }
    if request.is_ajax():
        html= render_to_string('share_article.html', context, request=request)
        return JsonResponse({'form':html})
    else: 
        return redirect('blog')




@login_required
def like_post(request, pk):
    if request.user.is_authenticated:
        article=blog_pulucia.objects.get(pk=pk)
        post=get_object_or_404(blog_pulucia, pk=pk) 
       
        is_liked=False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            is_liked=False
        else:
            post.likes.add(request.user)
            is_liked=True
        context={
            'post':post,
            'is_liked':is_liked,
            'total_likes':post.total_likes(),
            'article':article,
            
        }

        if request.is_ajax():
            html= render_to_string('like_section.html', context, request=request)
            return JsonResponse({'form':html})
    return redirect('login')


#--------- systeme commentaire Article------------------
@login_required
def comment_article1(request, pk):
    article=blog_pulucia.objects.get(pk=pk)
    commentaire=comment_article.objects.filter(article__pk=article.pk).order_by('-date')
    data = dict()
    form=comment_article_form()
    if request.method == 'POST':
        form=comment_article_form(request.POST)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.user=request.user
            form1.article=article
            form1.save() 
            data['form_is_valid'] = True
            context={
            'article':article,
            'commentaire':commentaire,

                }

            data['html_comment']= render_to_string('comment_article.html', context, request=request)
            return JsonResponse(data)
          
        else:
            data['form_is_valid'] = False
    context = {'form': form,
                'article':article}
    data['html_form'] = render_to_string('commentaire_form_article.html', context, request=request)
    return JsonResponse(data)


def blog(request):
    blog1=blog_pulucia.objects.all().order_by('-date')
    blog2=blog_pulucia.objects.all().order_by('-views')[:8] # les plus lus

    blog_search=articlefilter(request.GET, queryset=blog1)
    paginator=Paginator(blog_search.qs, 5)
    page=request.GET.get('page')
    #blog_search1=blog_search.qs
    try:
        blog_search1 = paginator.page(page)
    except PageNotAnInteger:
        blog_search1 = paginator.page(1)
    except EmptyPage:
        blog_search1 = paginator.page(paginator.num_pages)

    context={
        'blog1':blog_search1,
        'blog2':blog2,
        'blog_search': blog_search,
    }
    return render(request, 'blog.html', context)



def publication1(request):
    publication_details=publication.objects.all().order_by('?') # ?: mean order by random
    theme2=publication.objects.all()

    recent=publication.objects.all().order_by('-date')[:5]
    plus_lus=publication.objects.all().order_by('-views1')[:5]
    top=publication.objects.all().order_by('-views1')[:1]

    # associate django filter and pagination
    auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)
    paginator=Paginator(auteur_search.qs, 13)
    page=request.GET.get('page')

    try:
        publication_details1 = paginator.page(page)
    except PageNotAnInteger:
        publication_details1 = paginator.page(1)
    except EmptyPage:
        publication_details1 = paginator.page(paginator.num_pages)
    auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)


   
    #------------ get all the distinct theme----------#
    list1=[]
    for a in theme2:
        list1.append(a.theme)
    
    theme=[]
    for x in list1:
        if x not in theme:
            theme.append(x)
    #------------ get all the distinct theme----------#
    
    context={
        'publication1':publication_details1,
        'theme':theme,
         'recent':recent,
         'plus_lus':plus_lus,
         'top':top,
         'auteur_search': auteur_search,
        
    
    }
    return render(request, 'publication1.html', context)



def publication_search_categorie(request, slug):
    publication_details=publication.objects.filter(categorie=slug).order_by('?') # ?: mean order by random
    recent=publication.objects.all().order_by('-date')[:5]
    plus_lus=publication.objects.all().order_by('-views1')[:5]
    top=publication.objects.all().order_by('-views1')[:1]
    theme2=publication.objects.all()

    # associate django filter and pagination
    auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)
    paginator=Paginator(auteur_search.qs, 13)
    page=request.GET.get('page')

    try:
        publication_details1 = paginator.page(page)
    except PageNotAnInteger:
        publication_details1 = paginator.page(1)
    except EmptyPage:
        publication_details1 = paginator.page(paginator.num_pages)
    auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)


    list1=[]
    for a in theme2:
        list1.append(a.theme)
    
    theme=[]
    for x in list1:
        if x not in theme:
            theme.append(x)
    context={
        'publication1':publication_details1,
        'theme':theme,
        'recent':recent,
         'plus_lus':plus_lus,
         'top':top,
          'auteur_search': auteur_search,
      
    }
    return render(request, 'publication1.html', context)

def publication_search_theme(request, slug):
    publication_details=publication.objects.filter(theme__theme=slug).order_by('?') # ?: mean order by random
    recent=publication.objects.all().order_by('-date')[:5]
    plus_lus=publication.objects.all().order_by('-views1')[:5]
    top=publication.objects.all().order_by('-views1')[:1]
    theme2=publication.objects.all()

    # associate django filter and pagination
    auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)
    paginator=Paginator(auteur_search.qs, 13)
    page=request.GET.get('page')

    try:
        publication_details1 = paginator.page(page)
    except PageNotAnInteger:
        publication_details1 = paginator.page(1)
    except EmptyPage:
        publication_details1 = paginator.page(paginator.num_pages)
    auteur_search=auteur_pub_filter(request.GET, queryset=publication_details)

    

    #------------ get all the distinct theme----------#
    list1=[]
    for a in theme2:
        list1.append(a.theme)
    
    theme=[]
    for x in list1:
        if x not in theme:
            theme.append(x)
    #------------ get all the distinct theme----------#
    
    theme_par=slug
    
    context={
        'publication1':publication_details1,
        'theme':theme,
        'theme_par':theme_par,
        'recent':recent,
         'plus_lus':plus_lus,
         'top':top,
          'auteur_search': auteur_search,
        
       
         
    }
    return render(request, 'publication1.html', context)


def text1(request, pk):
    text_d=publication.objects.get(pk=pk)
    commentaire=comment_text2.objects.filter(text__pk=text_d.pk).order_by('-date')
    form=comment_text_form()
    total_comment=commentaire.count()
    auteur_m=publication.objects.filter(auteur__auteur=text_d.auteur).order_by('-date')
    total_auteur=auteur_m.count()

    recent=publication.objects.all().order_by('-date')[:5]
    plus_lus=publication.objects.all().order_by('-views1')[:5]
    top=publication.objects.all().order_by('-views1')[:1]

    text_d.views1+=1
    text_d.save()
    context={
        'text_d':text_d,
        'total_likes':text_d.total_likes(),
        'commentaire':commentaire,
        'total_comment':total_comment,
        'form':form,
        'auteur_m':auteur_m,
        'total_auteur':total_auteur,
        'recent':recent,
        'plus_lus':plus_lus,
        'top':top,
        
    }
    return render(request, 'text.html', context)

def share_text(request, pk):
    text_d=publication.objects.get(pk=pk)
    text_d.share1+=1
    text_d.save()
    context={
        'text_d':text_d,
    }
    if request.is_ajax():
        html= render_to_string('share-text.html', context, request=request)
        return JsonResponse({'form':html})
    else: 
        return redirect('blog')

@login_required
def like_text(request, pk):
    if request.user.is_authenticated:
        text_d=publication.objects.get(pk=pk)
        post=get_object_or_404(publication, pk=pk) 
       
        is_liked=False
        if post.likes1.filter(id=request.user.id).exists():
            post.likes1.remove(request.user)
            is_liked=False
        else:
            post.likes1.add(request.user)
            is_liked=True
        context={
            'post':post,
            'is_liked':is_liked,
            'total_likes':post.total_likes(),
            'text_d':text_d,
            
            }

        if request.is_ajax():
            html= render_to_string('text_like.html', context, request=request)
            return JsonResponse({'form':html})
    return redirect('login')

@login_required
def comment_text1(request, pk):
    text_d=publication.objects.get(pk=pk)
    commentaire=comment_text2.objects.filter(text__pk=text_d.pk).order_by('-date')
    data = dict()
    form=comment_text_form()
    if request.method == 'POST':
        form=comment_text_form(request.POST)
        if form.is_valid():
            form1=form.save(commit=False)
            form1.user=request.user
            form1.text=text_d
            form1.save() 
            data['form_is_valid'] = True
            context={
            'text_d':text_d,
            'commentaire':commentaire,

                }

            data['html_comment']= render_to_string('comment_text.html', context, request=request)
            return JsonResponse(data)
          
        else:
            data['form_is_valid'] = False
    context = {'form': form,
                'text_d':text_d}
    data['html_form'] = render_to_string('commentaire_form_text.html', context, request=request)
    return JsonResponse(data)


def temoignages(request):
    return render(request, 'temoignages.html')

def a_propos(request):
    return render(request, 'a-propos.html')

def projet_main(request):
    projet1=projet.objects.all().order_by('-date')
    context = {'projet1': projet1,
               }
    return render(request, 'projet.html', context)

def projet_details(request, pk):
    projet_d=projet.objects.get(pk=pk)
    
    context = {'projet_d': projet_d,
               }
    return render(request, 'projet-details.html', context)



def videos(request):
    videos1=video_youtube.objects.all().order_by('-date')
    context={
        'videos1':videos1

    }
    return render(request, 'videos.html', context)


