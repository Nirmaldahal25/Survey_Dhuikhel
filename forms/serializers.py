from rest_framework import serializers
from forms.models import (
    PersonsForm,
    PersonalSkills,
    InterestedOccupation,
    PersonTrainings,
    Occupation,
)


class InterestedOccupationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedOccupation
        fields = "__all__"


class PersonTrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTrainings
        fields = "__all__"


class PersonSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSkills
        fields = "__all__"


class OccupationSerializer(serializers.Serializer):
    class Meta:
        model = Occupation
        fields = "__all__"


class PersonsFormSerializer(serializers.ModelSerializer):
    skills = PersonSkillsSerializer(read_only=True, many=True)
    trainings = PersonTrainingsSerializer(read_only=True, many=True)
    interest_occupations = InterestedOccupationsSerializer(read_only=True, many=True)
    age = serializers.IntegerField(read_only=True)

    class Meta:
        model = PersonsForm
        fields = "__all__"
        extra_fields = ("skills", "trainings", "interest_occupations", "age")
