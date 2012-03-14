# Create your views here.
from django.template import Context, loader
from imnet.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
import simplejson

def index(request):
    Artists = Artist.objects.all()[:5]
    print request.user.is_authenticated()
    return render_to_response('imnet/index.html', {'artists': Artists},context_instance=RequestContext(request))


def artist(request,artist_id):
    try:
        a = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/artist.html', {'artist':a},context_instance=RequestContext(request))

def artist_tracks(request, artist_id):
    try:
        a = Artist.objects.get(pk=artist_id)
        tracks = a.track_set.all()
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/artist_tracks.html', {'artist':a, 'tracks':tracks},context_instance=RequestContext(request))

def artist_albums(request, artist_id):
    try:
        a = Artist.objects.get(pk=artist_id)
        albums = a.album_set.all()
        print a
        print albums
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/artist_albums.html', {'artist':a, 'albums':albums},context_instance=RequestContext(request))

def album(request, album_id):
    try:
        a = Album.objects.get(pk=album_id)
        tracks = a.track_set.all()
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/album.html', {'album':a, 'tracks':tracks},context_instance=RequestContext(request))


def artists(request):
    Artists = Artist.objects.all()[:]
    print Artists
    return render_to_response('imnet/artists.html', {'artists': Artists},context_instance=RequestContext(request))

def labels(request):
    Labels = Label.objects.all()[:]
    print Labels
    return render_to_response('imnet/labels.html', {'labels': Labels},context_instance=RequestContext(request))

def label(request,label_id):
    try:
        l = Label.objects.get(pk=label_id)
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/label.html', {'label':l},context_instance=RequestContext(request))

def label_albums(request, label_id):
    try:
        l = Label.objects.get(pk=label_id)
        albums = l.album_set.all()
        print albums
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/label_albums.html', {'label':l, 'albums':albums},context_instance=RequestContext(request))

def label_artists(request, label_id):
    try:
        l = Label.objects.get(pk=label_id)
        artists = l.artists.all()
        print artists
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/label_artists.html', {'label':l, 'artists':artists},context_instance=RequestContext(request))


def track(request, track_id):
    track = Track.objects.get(pk=track_id)

    return render_to_response('imnet/track.html', {'track': track})

def user_lookup(request, username):
    # Default return list
    results = []
    if username is not None:
        model_results = User.objects.filter(username__icontains=username)[:10]
        results = [ x.username for x in model_results ]
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')