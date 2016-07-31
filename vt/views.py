
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def index(req):
    return render(req, 'vt/index.html', {})


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


def video(req):
    videos = ExternalVideo.objects.order_by('order')
    return render(req, 'vt/video.html', {'videos' : videos})


def events(req):
    events = Event.objects.order_by('-start_date')
    return render(req, 'vt/events.html', {'events': events})


def contacts(req):
    return render(req, 'vt/contacts.html', {})


def testpage(req):
    return render(req, 'vt/testpage.html', {})


# free form pages

def pages(req):
    slug = req.path.rsplit('/', 1)[-1]
    page = get_object_or_404(Page, slug=slug)    
    return render(req, 'vt/page.html', {'page': page})


@login_required(login_url='/login')
def editpage(req):
    slug = req.GET['slug']
    page = get_object_or_404(Page, slug=slug)    
    return render(req, 'vt/editpage.html', {'page': page})


@login_required(login_url='/login')
def savepage(req):
    slug = req.POST['slug'] 
    Page.objects.update_or_create({
        'text': req.POST['text'],
        'lang':  req.POST['lang']
    }, slug=slug)
    return redirect('/vt/' + req.POST['slug'])
