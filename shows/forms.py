from django import forms

ATTRS_CLASS = 'SearchInput'

class SearchForm(forms.Form):
    """
    Formulaire de recherche.
    search : texte à rechercher (Cette valeur doit être codée par URI).
    """
    search = forms.CharField(label='Recherche',max_length=250)
    search.widget.attrs.update({'class': ATTRS_CLASS, 'placeholder' : "Rechercher"})