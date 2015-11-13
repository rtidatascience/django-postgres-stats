from django.db import models

class Checkin(models.Model):
    logged_at = models.DateTimeField()

class Number(models.Model):
    n = models.IntegerField()