from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.models import rpgclass, rpgrace
from media.models import Image


class zcharacter(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    rpgclass = models.ForeignKey(
        rpgclass, on_delete=models.PROTECT, related_name="zcharacter"
    )
    rpgrace = models.ForeignKey(
        rpgrace, on_delete=models.PROTECT, related_name="zcharacter"
    )
    img = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    def __str__(self):
        return ("Personagem de: " + self.name + " Feito por: ")

    class Meta:
        verbose_name_plural = "Characters"