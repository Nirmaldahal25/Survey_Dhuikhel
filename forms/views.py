from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework import status
from forms.models import (
    PersonsForm,
    PersonTrainings,
    EducationQualifications,
    PersonalSkills,
)
from forms.mixins import MultipleFieldLookupMixin
from forms.serializers import (
    PersonsFormSerializer,
    EducationQualificationsSerializer,
    PersonTrainingsSerializer,
    PersonSkillsSerializer,
)


class GenderView(APIView):
    def get(self, request, format=None):
        genders = PersonsForm.GENDER
        genders_dict = dict()
        for no, gender in genders:
            genders_dict[no] = gender

        return Response(data=genders_dict, status=status.HTTP_200_OK)


class WodaView(APIView):
    def get(self, request, format=None):
        wodas = PersonsForm.WODA
        wodas_dict = dict()
        for no, woda in wodas:
            wodas_dict[no] = woda

        return Response(data=wodas_dict, status=status.HTTP_200_OK)


class TrainingView(APIView):
    def get(self, request, format=None):
        trainings_dict = PersonTrainings.TRAININGS
        return Response(data=trainings_dict, status=status.HTTP_200_OK)


class ReligionView(APIView):
    def get(self, request, format=None):
        religion_dict = PersonsForm.RELIGION
        return Response(data=religion_dict, status=status.HTTP_200_OK)


class QualificationsView(APIView):
    def get(self, request, format=None):
        qualifications_dict = EducationQualifications.QUALIFICATION
        return Response(data=qualifications_dict, status=status.HTTP_200_OK)


class OccupationsView(APIView):
    def get(self, request, format=None):
        occupations_dict = PersonsForm.OCCUPATION
        return Response(data=occupations_dict, status=status.HTTP_200_OK)


class AdmiredOccuptionView(APIView):
    def get(self, request, format=None):
        ad_occupations_dict = PersonsForm.ADMIRED_OCCUPATION
        return Response(data=ad_occupations_dict, status=status.HTTP_200_OK)


class CasteView(APIView):
    def get(self, request, format=None):
        caste_dict = PersonsForm.CASTE
        return Response(data=caste_dict, status=status.HTTP_200_OK)


class PersonListCreateView(ListCreateAPIView):
    serializer_class = PersonsFormSerializer
    queryset = PersonsForm.objects.all()

    def get_queryset(self):
        queryset = super(PersonListCreateView, self).get_queryset()
        name = self.request.query_params.get("name")
        citizenship = self.request.query_params.get("citizenship")
        if name and citizenship:
            queryset = queryset.filter(name=name, citizenship=citizenship)
        return queryset


class PersonRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonsFormSerializer
    queryset = PersonsForm.objects.all()


class QualificationListCreateView(ListCreateAPIView):
    queryset = EducationQualifications.objects.all()
    serializer_class = EducationQualificationsSerializer
    lookup_field = "person"


class QualificationRUDView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = EducationQualifications.objects.all()
    serializer_class = EducationQualificationsSerializer
    lookup_fields = ("person", "pk")


class PersonsTrainingListCreateView(MultipleFieldLookupMixin, ListCreateAPIView):
    queryset = PersonTrainings.objects.all()
    serializer_class = PersonTrainingsSerializer
    lookup_field = "person"


class PersonsTrainingRUDView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = PersonTrainings.objects.all()
    serializer_class = PersonTrainingsSerializer
    lookup_fields = ("person", "pk")


class PersonSkillListCreateView(ListCreateAPIView):
    queryset = PersonalSkills.objects.all()
    serializer_class = PersonSkillsSerializer
    lookup_field = "person"


class PersonSkillRUDView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = PersonalSkills.objects.all()
    serializer_class = PersonSkillsSerializer
    lookup_fields = ("person", "pk")
