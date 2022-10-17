import math
from django.db import models

# Create your models here.


class Sexes(models.TextChoices):
    MALE = 'Macho'
    FEMALE = 'Fêmea'
    UNINFORMED = 'Não informado'


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=15,
        choices=Sexes.choices,
        default=Sexes.UNINFORMED,
    )
    group = models.ForeignKey(
        'groups.Group', 
        on_delete=models.CASCADE,
        related_name='animals',
        null=True
    )
    traits = models.ManyToManyField(
        'traits.Trait',
        related_name='traits'
    )

    def dog_to_human_years(self) -> int:
        return 16 * math.log(self.age) + 31
