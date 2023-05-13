from rest_framework import serializers
from forms.models import (
    PersonsForm,
    PersonalSkills,
    EducationQualifications,
    PersonTrainings,
)


class EducationQualificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationQualifications
        fields = "__all__"


class PersonTrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonTrainings
        fields = "__all__"


class PersonSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalSkills
        fields = "__all__"


class PersonsFormSerializer(serializers.ModelSerializer):
    skills = PersonSkillsSerializer(many=True)
    trainings = PersonTrainingsSerializer(many=True)
    qualifications = EducationQualificationsSerializer(many=True)

    class Meta:
        model = PersonsForm
        fields = "__all__"
        extra_fields = ("skills", "trainings", "qualifications")

    def create(self, validated_data):
        skills = validated_data.pop("skills")
        trainings = validated_data.pop("trainings")
        qualifications = validated_data.pop("qualifications")
        instance = super(PersonsFormSerializer, self).create(validated_data)

        for skill in skills:
            _ = PersonalSkills.objects.create(person=instance, **skill)

        for training in trainings:
            _ = PersonTrainings.objects.create(person=instance, **training)

        for qualification in qualifications:
            _ = EducationQualifications.objects.create(person=instance, **qualification)

        return instance

    def update(self, instance, validated_data):
        skills = validated_data.pop("skills")
        trainings = validated_data.pop("trainings")
        qualifications = validated_data.pop("qualifications")
        instance = super(PersonsFormSerializer, self).update(instance, validated_data)

        for skill in skills:
            try:
                sk = instance.personalskills_set.get(id=skill.get("id", None))
                for key, value in dict(skill).items():
                    setattr(sk, key, value)
                sk.save()
            except PersonalSkills.DoesNotExist:
                pass

        for training in trainings:
            try:
                tr = instance.persontrainings_set.get(id=training.get("id", None))
                for key, value in dict(training).items():
                    setattr(tr, key, value)
                tr.save()
            except PersonTrainings.DoesNotExist:
                pass

        for qualification in qualifications:
            try:
                ql = instance.educationqualifications_set.get(
                    id=qualification.get("id", None)
                )
                for key, value in dict(qualification).items():
                    setattr(ql, key, value)
                ql.save()
            except EducationQualifications.DoesNotExist:
                pass

        return instance
