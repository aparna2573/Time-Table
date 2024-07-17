from typing import Required
from django import  forms
from django.forms.fields import TextInput, re 

class teacher_view(forms.Form):
    teacher_code = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Teacher Code',  'class': 'form-control'}),required = False)

    subject_code = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Subject Code',  'class': 'form-control'}), required = False)

class student_view(forms.Form):
    semester = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Semester',  'class': 'form-control'}), required = False)

    Batch = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Batch',  'class': 'form-control'}), required = False)
    subject_code = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Subject Code',  'class': 'form-control'}), required = False)
