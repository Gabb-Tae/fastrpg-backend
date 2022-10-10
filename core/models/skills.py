from django.db import models
from core.models import rpgclass
        

class skills(models.Model):
    description = models.CharField(max_length=1000)
    rpgclass = models.ForeignKey(
        rpgclass, on_delete=models.PROTECT, related_name="skills"
    )
    def __str__(self):
        return (self.rpgclass.name + " - " + self.description)
    class Meta:
        verbose_name_plural = "Skills"
