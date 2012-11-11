from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=512)

class Member(models.Model):
    fname = models.CharField('First Name', max_length=200)
    sname = models.CharField('Last Name', max_length=200)
    club = models.ForeignKey(Club)
