from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm, SentimentForm
from .sentiment_classification import predict, process_sentiment


def index(request):
    chats = Chat.objects.all() #List of chats
    return render(request, 'main/index.html', {'chats': chats})


def create_chat(request):
    error = ''
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Wrong form'
    form = ChatForm()
    return render(request, 'main/create_chat.html', {'form': form, 'error': error})


def check_sentiment(request):
    result = ''
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid:
            result = process_sentiment(form['message_text'].value())
        else:
            result = 'Wrong form'
    form = SentimentForm()
    return render(request, 'main/check_sentiment.html', {'form': form, 'result': result})

def about(request):
    return render(request, 'main/about.html')
