from django.db import models


class User(models.Model):
    user_id = models.IntegerField('user_id')
    user_name = models.CharField('user_name', max_length=50)

    def __str__(self):
        return self.user_name


class Chat(models.Model):
    chat_id = models.IntegerField('chat_id', primary_key=True)
    chat_title = models.CharField('chat_title', max_length=50)
    chat_messages_count = models.IntegerField('chat_messages_count', default=0)

    def __str__(self):
        return f'{self.chat_title} - id:{self.chat_id} - msg:{self.chat_messages_count}'


class Message(models.Model):
    from_chat_id = models.IntegerField('from_chat_id')
    from_user_id = models.IntegerField('from_user_id')
    message_id = models.IntegerField('message_id')
    message_text = models.CharField('message_text', max_length=250)

    def __str__(self):
        return self.message_text
