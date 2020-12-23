from django.db import models
from django.db import models
# Create your models here.


class HeroInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()

    def __str__(self):
        return self.name


class SkillInfo(models.Model):
    name = models.CharField(max_length=10)
    hero = models.ForeignKey(HeroInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
