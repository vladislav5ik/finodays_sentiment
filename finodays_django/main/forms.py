from .models import Chat
from django.forms import ModelForm, TextInput, Textarea, Form, CharField


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ["chat_title"]
        widgets = {
            "chat_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter chat name'
            })
        }


class SentimentForm(Form):
    message_text = CharField(label='message_text',
                             max_length=1000,
                             widget=Textarea(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter text'
                                                    }))
