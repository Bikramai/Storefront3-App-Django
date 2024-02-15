from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message', 'from@mangbuy.com', ['Hang@mangbuy.com'])
        message.attach_file('playground/static/images/git.png')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Bikram'})
