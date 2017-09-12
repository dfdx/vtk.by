
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from vt.models import *
from vingtsunkuen.models import *

THIS_SITE = 'sr'

def info(req):
    return render(req, 'sr/info.html', {})


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
    return render(req, 'sr/photo.html', {'categories' : categories})


# free form pages

def viewpage(req):
    slug = req.path.rsplit('/', 1)[-1]
    # site = req.path.rsplit('/', 1)[-2].strip('/')
    pages = Page.objects.filter(slug=slug, site=THIS_SITE)
    if len(pages) == 1:        
        return render(req, 'sr/page.html', {'page': pages[0]})
    else:
        return render(req, 'sr/page-doesnt-exist.html', {'slug': slug})


@login_required(login_url='/login')
def editpage(req):
    slug = req.GET['slug']
    pages = Page.objects.filter(slug=slug, site=THIS_SITE)
    if len(pages) == 1:
        return render(req, 'sr/editpage.html', {'page': pages[0]})
    else:
        new_page = Page(slug=slug, text='', lang='markdown')
        return render(req, 'sr/editpage.html', {'page': new_page})
        
    
@login_required(login_url='/login')
def savepage(req):
    slug = req.POST['slug']    
    Page.objects.update_or_create({
        'text': req.POST['text'],
        'lang':  req.POST['lang'],
    }, slug=slug, site=THIS_SITE)
    return redirect('/sr/' + req.POST['slug'])

