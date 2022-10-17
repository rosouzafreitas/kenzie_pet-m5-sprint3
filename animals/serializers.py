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
    age_in_human_years = serializers.SerializerMethodField(read_only = True)
    group = GroupSerializer()
    traits = TraitSerializer(many = True)
    
    def get_age_in_human_years(self, obj: Animal):
        return obj.dog_to_human_years()
    
    def create(self, data: dict):
        group_data = data.pop('group')
        traits_data = data.pop('traits')

        new_group, _ = Group.objects.get_or_create(**group_data)

        new_animal = Animal.objects.create(**data, group = new_group)

        for trait in traits_data:
            new_trait, _ = Trait.objects.get_or_create(**trait)
            new_animal.traits.add(new_trait)
        new_animal.save()

        return new_animal


    def update(self, instance: Animal, data: dict):
        errors = {}
        constants = {
            'sex': str,
            'traits': Trait,
            'group': Group,
        }

        for data in constants.keys():
            if data in data:
                msg = {f'{data}': f'You can not update {data} property.'}
                errors.update(msg)

        for key, value in data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
        