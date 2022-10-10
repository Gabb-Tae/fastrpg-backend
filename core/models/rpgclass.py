from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from core.models import itens

class rpgclass(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=700)
    life = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
    main_skill = models.CharField(max_length=20)
    strength = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    dexterity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    constitution = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    intelligence = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    wisdom = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    charism = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    itens = models.ManyToManyField(itens, related_name="rpgclass")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Classes"