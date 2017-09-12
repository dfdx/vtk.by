
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from vingtsunkuen.models import *
from itertools import groupby

THIS_SITE = 'vt'


def news(req):
    news = News.objects.order_by('-pub_date')
    return render(req, 'vt/news.html', {'all_news': news})


def address(req):
    return render(req, 'vt/address.html')


def schedule(req):
    trainings = ScheduledTraining.objects.order_by('day').all()
    return render(req, 'vt/schedule.html', {'trainings' : trainings})


def photo(req):
    albums = PhotoAlbum.objects.filter(site=THIS_SITE)
    cat_dict = {}
    for album in albums:
        if album.category not in cat_dict:
            cat_dict[album.category] = []
        cat_dict[album.category].append(album)
    cats_sorted = sorted(cat_dict.items(), key=lambda t: t[0].order)
    categories = [(c, sorted(als, key=lambda a: a.order))
                  for c, als in cats_sorted]
    return render(req, 'vt/photo.html', {'categories' : categories})


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

def viewpage(req):
    slug = req.path.rsplit('/', 1)[-1]
    # site = req.path.rsplit('/', 1)[-2].strip('/')
    pages = Page.objects.filter(slug=slug, site=THIS_SITE)
    if len(pages) == 1:
        return render(req, 'vt/page.html', {'page': pages[0]})
    else:
        return render(req, 'vt/page-doesnt-exist.html', {'slug': slug})


@login_required(login_url='/login')
def editpage(req):
    slug = req.GET['slug']
    pages = Page.objects.filter(slug=slug, site=THIS_SITE)
    if len(pages) == 1:
        return render(req, 'vt/editpage.html', {'page': pages[0]})
    else:
        new_page = Page(slug=slug, text='', lang='markdown')
        return render(req, 'vt/editpage.html', {'page': new_page})



@login_required(login_url='/login')
def savepage(req):
    slug = req.POST['slug']
    Page.objects.update_or_create({
        'text': req.POST['text'],
        'lang':  req.POST['lang'],
    }, slug=slug, site=THIS_SITE)
    return redirect('/vt/' + req.POST['slug'])
