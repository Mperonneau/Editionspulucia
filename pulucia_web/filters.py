import django_filters
from django_filters import CharFilter
from django.forms.widgets import TextInput
from .models import *
from django.db.models import Q


class auteur_pub_filter(django_filters.FilterSet):
    auteur__auteur = django_filters.CharFilter(lookup_expr='icontains', widget=TextInput(attrs={'placeholder': "Recherche d'auteur"}))
    class Meta:
        model = publication
        fields = ['auteur__auteur']


class articlefilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', widget=TextInput(attrs={'placeholder': "Recherche"}))

    class Meta:
        model = blog_pulucia
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return blog_pulucia.objects.filter(
            Q(titre__icontains=value) | Q(redacteur__icontains=value) | Q(text__icontains=value)) 

class librairiefilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', widget=TextInput(attrs={'placeholder': "Recherche"}))

    class Meta:
        model = livre_librairie
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return livre_librairie.objects.filter(
            Q(titre_du_livre__icontains=value) | Q(auteur__icontains=value)) 


class bibliothequefilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', widget=TextInput(attrs={'placeholder': "Recherche"}))

    class Meta:
        model = bibliotheque1
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return bibliotheque1.objects.filter(
            Q(titre__icontains=value) | Q(auteur__icontains=value)) 








