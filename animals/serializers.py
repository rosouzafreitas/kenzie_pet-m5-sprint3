from rest_framework import serializers
from animals.models import Animal, Sexes
from groups.models import Group
from traits.models import Trait
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices = Sexes.choices,
        default = Sexes.UNINFORMED,
    )
    dog_to_human_years = serializers.SerializerMethodField(read_only = True)
