from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=512)

class Person(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)
    notes = models.TextField()
    comany = models.ForeignKey(Company)
