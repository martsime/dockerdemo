from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Case(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)

