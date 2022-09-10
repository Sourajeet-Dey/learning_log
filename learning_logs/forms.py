from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'placeholder': 'Type here...'})}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'placeholder': 'Start typing/writing here...', 'cols': 100,   'rows': 10})}