from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from media.models import Image


class itens(models.Model):
    name = models.CharField(max_length=100)
    definition = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Itens"
        
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

class skills(models.Model):
    description = models.CharField(max_length=1000)
    rpgclass = models.ForeignKey(
        rpgclass, on_delete=models.PROTECT, related_name="skills"
    )
    def __str__(self):
        return (self.rpgclass.name + " - " + self.description)
    class Meta:
        verbose_name_plural = "Skills"

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

class character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    rpgclass = models.ForeignKey(
        rpgclass, on_delete=models.PROTECT, related_name="character"
    )
    rpgrace = models.ForeignKey(
        rpgrace, on_delete=models.PROTECT, related_name="character"
    )
    img = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    class Meta:
        verbose_name_plural = "Characters"