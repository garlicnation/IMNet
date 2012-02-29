# Create your views here.
from django.template import Context, loader
from imnet.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

@login_required
def index(request):
    Artists = Artist.objects.all()[:5]
    t = loader.get_template('imnet/index.html')
    c = Context({
        'artists': Artists,
        })
    return HttpResponse(t.render(c))


def artist(request,artist_id):
    try:
        a = Artist.objects.get(pk=artist_id)
    except Artist.DoesNotExist:
        raise Http404
    return render_to_response('imnet/artist.html', {'artist':a})

def artists(request):
    Artists = Artist.objects.all()[:]
    print Artists
    return render_to_response('imnet/artists.html', {'artists': Artists})