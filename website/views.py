from django.shortcuts import render, redirect
from django import views
from django.core.mail import send_mail

class HomeView(views.View):
    def get(self, request):
        return render(request, 'website/home.html', {})

    def post(self, request):
        mail_body = f'Name: {request.POST.get("name")}\nSurname: {request.POST.get("surname")}\nEmail: {request.POST.get("email")}\nMessage: \n{request.POST.get("message")}'

        send_mail(
            'From PORFOLIO: New message!',
            mail_body,
            'ruth.fernandez.mk.2020@gmail.com', 
            [
                'martinjafactor@gmail.com',
            ],
        )

        return redirect('home')
