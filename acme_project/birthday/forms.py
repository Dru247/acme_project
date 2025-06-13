from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            )
        }

    def clean_first_name(self):
        """Сокращает составное имя до 1го слова."""
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        """Проверка полей на идентичность Битлс."""
        # Вызов родительского метода clean (уникальность записи).
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )
