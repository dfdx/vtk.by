
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def index(req):
    return render(req, 'vt/main.html', {})


def loginpage(req):
    """Login page"""
    next_page = req.GET.get('next')
    return render(req, 'vt/login.html', {'next_page': next_page})


def signin(req):
    """Perform sign in"""
    username = req.POST['username']
    password = req.POST['password']
    next_page = req.GET.get('next')
    print(req.GET)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(req, user)
            if next_page:
                return redirect(next_page)
            else:
                return redirect('/')
        else:
            return render(req, 'vt/login.html',
                          {'error_message' : 'Пользователь не активен'})
    else:        
        return render(req, 'vt/login.html',
                      {'error_message' : 'Неверный логин и/или пароль'})

    
def signout(req):
    logout(req)
    return redirect('/')


def news(req):
    news = News.objects.order_by('-pub_date')
    return render(req, 'vt/news.html', {'all_news': news})


def address(req):
    return render(req, 'vt/address.html')


def schedule(req):
    trainings = ScheduledTraining.objects.order_by('day').all()    
    return render(req, 'vt/schedule.html', {'trainings' : trainings})


@login_required(login_url='/login')
def video(req):
    return render(req, 'vt/video.html', {})


def events(req):
    return render(req, 'vt/events.html', {})


def contacts(req):
    return render(req, 'vt/contacts.html', {})


def join(req):
    return render(req, 'vt/join.html', {})


def shinkage(req):
    return render(req, 'vt/shinkage.html', {})

