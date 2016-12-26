
from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from PIL import Image
import boto3
import os.path
import json

def index(req):
    return render(req, 'vingtsunkuen/index.html', {})


def loginpage(req):
    """Login page"""
    next_page = req.GET.get('next')
    return render(req, 'vingtsunkuen/login.html', {'next_page': next_page})


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
            return render(req, 'vingtsunkuen/login.html',
                          {'error_message' : 'Пользователь не активен'})
    else:
        return render(req, 'vingtsunkuen/login.html',
                      {'error_message' : 'Неверный логин и/или пароль'})


def signout(req):
    logout(req)
    return redirect('/')


s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

def store_image(folder, afile):
    tmpfile_name = '/tmp/%s' % (afile.name)
    with open(tmpfile_name, 'wb') as tmpfile:
        tmpfile.write(afile.read())
    with Image.open(tmpfile_name) as im:
        w, h = im.size
    name, ext = os.path.splitext(afile.name)
    new_name = name + '_' + str(w) + '_' + str(h) + ext
    with open(tmpfile_name, 'rb') as tmpfile:
        s3.Bucket('vingtsunkuen').put_object(Key=folder + '/' + new_name, Body=tmpfile)
    os.remove(tmpfile_name)


@login_required(login_url='/login')
def upload_image(req):
    for afile in req.FILES.getlist('files'):
        store_image(req.POST['folder'], afile)
    return redirect(req.META['HTTP_REFERER'])


def _get_key_url(s3_client, bucket_name, key):
    params = {'Bucket': bucket_name, 'Key': key}
    url = s3_client.generate_presigned_url('get_object',
                                           Params = params,
                                           ExpiresIn = 3600)
    return url


def _image_size_from_url(url):
    filename = os.path.basename(url.split('?')[0])
    filename_no_ext = os.path.splitext(filename)[0]
    ws, hs = filename_no_ext.split('_')[-2:]
    return int(ws), int(hs)


def photo_gallery(req):
    folder = req.GET['folder']    
    bucket = s3.Bucket(name='vingtsunkuen')
    keys = [o.key for o in bucket.objects.filter(Prefix=folder).all()]
    urls = [_get_key_url(s3_client, 'vingtsunkuen', key) for key in keys]
    sizes = [_image_size_from_url(url) for url in urls]
    images = [(url, sz[0], sz[1]) for url, sz in zip(urls, sizes)]
    items = [{'src': url, 'w': w, 'h': h} for url, w, h in images]
    return HttpResponse(json.dumps(items))
