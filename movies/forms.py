from django import forms

ATTRS_CLASS = 'SearchIconeBox'

class SearchForm(forms):
    """
    Formulaire de recherche.
    search : texte à rechercher (Cette valeur doit être codée par URI).
    """
    search = forms.CharField(label='Recherche',max_length=250)
    search.widget.attrs.update({'class': ATTRS_CLASS})