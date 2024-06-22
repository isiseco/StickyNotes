from django import forms 
from .models import Note, Bulletin

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ['title', 'content']