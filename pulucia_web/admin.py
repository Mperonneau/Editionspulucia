from django.contrib import admin
from .models import *

admin.site.register(inscription)
admin.site.register(livre_librairie)
admin.site.register(point_vente_livre)
admin.site.register(librairie_categorie)


# methode to make a field read_only in model
class read_only1(admin.ModelAdmin):
    fields = ['titre','redacteur', 'categorie','text', 'image', 'image_source','views','likes', 'share']
    readonly_fields = ['views', 'likes']

class read_only2(admin.ModelAdmin):
    fields = ['auteur','theme', 'categorie','titre', 'poeme','text', 'couleur','views1','likes1', 'share1']
    readonly_fields = ['views1','likes1','share1']

class read_only3(admin.ModelAdmin):
    fields = ['user','text', 'comment']
    readonly_fields = ['user','text','comment']

class read_only4(admin.ModelAdmin):
    fields = ['titre','auteur', 'categorie','document', 'image_cover', 'book_add']
    readonly_fields = ['book_add']

admin.site.register(blog_pulucia, read_only1)
admin.site.register(comment_article)
admin.site.register(evenement_main)
admin.site.register(evenement_photo)
admin.site.register(publication_auteur)
admin.site.register(publication, read_only2)
admin.site.register(publication_theme)
admin.site.register(comment_text2, read_only3)
admin.site.register(video_youtube)
admin.site.register(projet)
admin.site.register(bibliotheque_domaine)
admin.site.register(bibliotheque1,  read_only4)
admin.site.register(carousel_image)
admin.site.register(affiche1)





# Register your models here.
