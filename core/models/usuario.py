from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    school_class = models.CharField(max_length=11)
    birth_date = models.DateField(blank=True, null=True)