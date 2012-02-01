from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class MusicEntity(models.Model):
    name = models.CharField(max_length=128)
    owners = models.ManyToManyField(User)
    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

class Artist(MusicEntity):
    pass

class Label(MusicEntity):
    artists = models.ManyToManyField(Artist)

class Venue(MusicEntity):
    pass

class Music(models.Model):
    name = models.CharField(max_length=128)
    collaborators = models.ManyToManyField(Artist)

class Image(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User)

class Message(models.Model):
    subject = models.CharField(max_length=128)
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='sent')
    recipients = models.ManyToManyField(User, related_name='received')
