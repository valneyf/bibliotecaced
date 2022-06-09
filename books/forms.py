from dataclasses import fields
from django.forms import ModelForm
from django import forms
from formValidationApp.models import *
from django.core.exceptions import ValidationError

from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book

        fields = [
            'name',
            'category',
            'image',
            'author',
            'published',
            'pages',
        ]

    def clean(self):

        super(BookForm, self).clean()

        name = self.cleaned_data.get('name')
        published = self.cleaned_data.get('published')
        pages = self.cleaned_data.get('pages')

        if len(name) < 1:
            self._errors['name'] = self.error_class([
                'O título não pode ser vazio'
            ])
        if published < 1500 | published > 2022:
            self._errors['published'] = self.error_class([
                'O ano de publicação deve estar entre 1500 à 2022'
            ])
        if pages < 1:
            self._errors['pages'] = self.error_class([
                'O número de páginas não pode ser menor que 1'
            ])

        matching_books = Book.objects.filter(name=name)
        if self.instance:
            matching_books = matching_books.exclude(pk=self.instance.pk)
        if matching_books.exists():
            msg = u"Um livro com este título: %s já foi registrado." % name
            raise ValidationError(msg)
        else:
            return self.cleaned_data

    class Meta:
        model = Book
