from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class rpgrace(models.Model):
    name = models.CharField(max_length=50)
    features = models.CharField(max_length=700)
    size = models.CharField(max_length=20)
    speed = models.CharField(max_length=20)
    languages = models.CharField(max_length=60)
    strength = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    dexterity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    constitution = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    intelligence = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    wisdom = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    charism = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Races"
