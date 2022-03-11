from django import forms
from main.models import Movie


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['title', 'category', 'price', 'description', 'director', 'price_ticket']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Введите название',
                                            'class': 'form-control'}),
            'description': forms.TextInput(attrs={'placeholder': 'Описание фильма',
                                                  'class': 'form-control'}),
            'cinema': forms.TextInput(attrs={'placeholder': 'Введите название кинотеатра',
                                             'class': 'form-control'}),
            'price_ticket': forms.NumberInput(attrs={'placeholder': 'Введите стоимость билета',
                                                     'class': 'form-control'}),
            'category': forms.Select(attrs={'placeholder': 'Выберите категорию',
                                            'class': 'form-control'}),
            'genre': forms.Select(attrs={'placeholder': 'Выберите жанр',
                                         'class': 'form-control'}),
            'director': forms.TextInput(attrs={'placeholder': 'Режиссёр фильма',
                                               'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Стоимость онлайн трансляции',
                                              'class': 'form-control'}),
        }
