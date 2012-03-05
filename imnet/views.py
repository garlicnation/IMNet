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

def artists(request):
    Artists = Artist.objects.all()[:]
    print Artists
    return render_to_response('imnet/artists.html', {'artists': Artists},context_instance=RequestContext(request))


def user_lookup(request, username):
    # Default return list
    results = []
    if username is not None:
        model_results = User.objects.filter(username__icontains=username)[:10]
        results = [ x.username for x in model_results ]
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')