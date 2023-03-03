from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название статьи',
                'class': 'add-form'
            }),
            'text': Textarea(attrs={
                'placeholder': 'Текст статьи',
                'class': 'add-form'
            }),
            'date': DateTimeInput(attrs={
                'placeholder': 'Дата создания статьи',
                'class': 'add-form'
            })
        }
