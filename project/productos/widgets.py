from django import forms
from django.forms.widgets import ClearableFileInput


class MultipleFileInput(ClearableFileInput):
    template_name = 'widgets/multiple_file_input.html'
    initial_text = 'Seleccionar archivos'
    input_text = 'Cambiar'
    clear_checkbox_label = 'Borrar selección'
    multiple = True  # Permite la selección múltiple de archivos

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['multiple'] = self.multiple
        return context


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result