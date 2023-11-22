from .models import Drive
from django.forms import ModelForm, TextInput, Textarea, EmailInput, Select


class DriveForm(ModelForm):
    class Meta:
        model = Drive
        fields = ["name", "phone", "email", "auto", "comment"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "auto": Select(attrs={
                'class': 'form-control',
            }, choices=[('Nissan Almera', 'Nissan Almera'),
                        ('Nissan Qashqai', 'Nissan Qashqai'),
                        ('Nissan Murano', 'Nissan Murano')]),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }
