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
        print a
        print tracks
        print tracks[0].file._get_url()
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

def artists(request):
    Artists = Artist.objects.all()[:]
    print Artists
    return render_to_response('imnet/artists.html', {'artists': Artists},context_instance=RequestContext(request))

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