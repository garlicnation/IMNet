from django.db import models
from django.contrib.auth.models import User

class MusicEntity(models.Model):
    name = models.CharField(max_length=128)
    shortname = models.CharField(max_length=20)
    description = models.TextField()
    owners = models.ManyToManyField(User)
    fans = models.ManyToManyField(User, related_name='favorites',blank=True, null=True)
    genre = models.TextField()
    website = models.URLField()
    main_image = models.ForeignKey('Image', blank=True, null=True)
    def __unicode__(self):
        return self.name

class Artist(MusicEntity):
    pass

class Label(MusicEntity):
    artists = models.ManyToManyField(Artist)

class Venue(MusicEntity):
    location = models.TextField()

class Event(MusicEntity):
    artists = models.ManyToManyField(Artist)
    venue = models.ForeignKey(Venue)
    date = models.DateTimeField()

class Album(models.Model):
    title = models.CharField(max_length=128)
    label = models.ForeignKey(Label)
    collaborators = models.ManyToManyField(Artist)
    description = models.TextField()
    release_date = models.DateField()
    cover_art = models.ImageField(upload_to='album_images/', blank=True, null=True)
    def __unicode__(self):
        return self.title

class Track(models.Model):
    title = models.CharField(max_length=128)
    number = models.IntegerField()
    genre = models.CharField(max_length=60)
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, blank=True, null=True)
    length = models.IntegerField() #Length in seconds
    file = models.FileField(upload_to='music/')
    def __unicode__(self):
        return self.title

class Image(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(MusicEntity)
    image = models.ImageField(upload_to='images/')
    def __unicode__(self):
        return self.name

class Message(models.Model):
    subject = models.CharField(max_length=128)
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='sent')
    recipients = models.ManyToManyField(User, related_name='received')

class Post(models.Model):
    author = models.ForeignKey(MusicEntity)
    title = models.CharField(max_length=128)
    body = models.TextField()