# Generated by Django 3.2.7 on 2021-09-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210911_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='id',
        ),
        migrations.AlterField(
            model_name='chat',
            name='chat_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='chat_id'),
        ),
    ]