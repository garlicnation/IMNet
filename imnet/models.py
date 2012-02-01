from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class MusicEntity(models.Model):
    name = models.CharField(max_length=128)
    shortname = models.CharField(max_length=20)
    description = models.TextField()
    owners = models.ManyToManyField(User)
    fans = models.ManyToManyField(User, related_name='favorites')
    genre = models.TextField()
    website = models.URLField()
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
#    cover_art = models.ImageField()

class Track(models.Model):
    title = models.CharField(max_length=128)
    number = models.IntegerField()
    genre = models.CharField(max_length=60)
    artists = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album)
    length = models.IntegerField() #Length in seconds

class Image(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(MusicEntity)

class Message(models.Model):
    subject = models.CharField(max_length=128)
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='sent')
    recipients = models.ManyToManyField(User, related_name='received')

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()