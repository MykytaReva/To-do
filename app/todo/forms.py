from django import forms
from todo.models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = (
            'subject',
            'date_todo',
            'status',
        )
        # widgets = {
        #     'date_todo': forms.DateField(widjet=forms.DateInput)
        # }