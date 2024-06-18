from django.forms.widgets import ClearableFileInput

class MultipleFileInput(ClearableFileInput):
    template_name = 'widgets/multiple_file_input.html'
    input_type = 'file'
    initial_text = 'Seleccionar archivos'
    input_text = 'Cambiar'
    clear_checkbox_label = 'Borrar selección'
    multiple = True

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs'].pop('multiple', None)  # Remove 'multiple' attribute
        return context