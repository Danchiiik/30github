
from choose_me.celery import app
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@app.task
def send_act_code_celery(email, code):
    link = f'http://localhost:8000/api/v1/users/confirm/{code}/'
    
    email_message = EmailMultiAlternatives(
        'Ваш код для активации аккаунта',
        link ,
        'dcabatar@gmail.com',
        [email]
    )
    email_message.send()


@app.task    
def send_confirmation_code(email, code):
    
    email_message = EmailMultiAlternatives(
        'Код для восстановления пароля',
        code ,
        'dcabatar@gmail.com',
        [email]
    )
    email_message.send()
