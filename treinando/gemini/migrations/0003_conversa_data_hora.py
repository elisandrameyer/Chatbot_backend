# Generated by Django 5.0.6 on 2024-06-16 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemini', '0002_remove_pergunta_indicador_conversa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversa',
            name='data_hora',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 16, 16, 46, 28, 790318)),
        ),
    ]
