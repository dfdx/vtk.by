
from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    return render(req, 'vt/main.html', {})

def address(req):
    return render(req, 'vt/address.html', {})

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

