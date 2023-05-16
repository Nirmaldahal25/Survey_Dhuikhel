from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework import status
from django.db.models import Count
from forms.models import (
    PersonsForm,
    PersonTrainings,
    InterestedOccupation,
    PersonalSkills,
)
from forms.mixins import MultipleFieldLookupMixin
from forms.serializers import (
    PersonsFormSerializer,
    InterestedOccupationsSerializer,
    PersonTrainingsSerializer,
    PersonSkillsSerializer,
)
from django.views.generic import TemplateView


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
        trainings_dict = PersonTrainings.TRAININGS.copy()
        trainings = (
            PersonTrainings.objects.all()
            .exclude(training__in=list(trainings_dict.values()))
            .values("training")
            .distinct()
        )
        data = len(PersonTrainings.TRAININGS)
        for value in trainings.values_list("training"):
            if value[0]:
                data += 1
                trainings_dict[data] = value[0]
        trainings_dict[data + 1] = "अन्य"
        return Response(data=trainings_dict, status=status.HTTP_200_OK)


class ReligionView(APIView):
    def get(self, request, format=None):
        religion_dict = PersonsForm.RELIGION.copy()
        religions = (
            PersonsForm.objects.all()
            .exclude(religion__in=list(religion_dict.values()))
            .values("religion")
            .distinct()
        )
        data = len(PersonsForm.RELIGION)
        for value in religions.values_list("religion"):
            if value[0]:
                data += 1
                religion_dict[data] = value[0]
        religion_dict[data + 1] = "अन्य"
        return Response(data=religion_dict, status=status.HTTP_200_OK)


class QualificationsView(APIView):
    def get(self, request, format=None):
        qualifications_dict = PersonsForm.QUALIFICATION.copy()
        qualifications = (
            PersonsForm.objects.all()
            .exclude(qualification__in=list(qualifications_dict.values()))
            .values("qualification")
            .distinct()
        )
        data = len(PersonsForm.QUALIFICATION)
        for value in qualifications.values_list("qualification"):
            data += 1
            qualifications_dict[data] = value[0]
        qualifications_dict[data + 1] = "अन्य"
        return Response(data=qualifications_dict, status=status.HTTP_200_OK)


class OccupationsView(APIView):
    def get(self, request, format=None):
        occupations_dict = PersonsForm.OCCUPATION.copy()
        occupations = (
            PersonsForm.objects.all()
            .exclude(occupation__in=list(occupations_dict.values()))
            .values("occupation")
            .distinct()
        )
        data = len(PersonsForm.OCCUPATION)
        for value in occupations.values_list("occupation"):
            data += 1
            occupations_dict[data] = value[0]
        occupations_dict[data + 1] = "अन्य"
        return Response(data=occupations_dict, status=status.HTTP_200_OK)


class PersonalSkillsView(APIView):
    def get(self, request, format=None):
        skills_dict = {}
        skills = PersonalSkills.objects.all().values("skills").distinct()
        data = 0
        for value in skills.values_list("skills"):
            data += 1
            skills_dict[data] = value[0]

        skills_dict[data + 1] = "अन्य"
        return Response(data=skills_dict, status=status.HTTP_200_OK)


class AdmiredOccuptionView(APIView):
    def get(self, request, format=None):
        ad_occupations_dict = InterestedOccupation.ADMIRED_OCCUPATION.copy()
        admired_occupations = (
            InterestedOccupation.objects.all()
            .exclude(interested_occupation__in=list(ad_occupations_dict.values()))
            .values("interested_occupation")
            .distinct()
        )
        data = len(InterestedOccupation.ADMIRED_OCCUPATION)
        for value in admired_occupations.values_list("interested_occupation"):
            data += 1
            ad_occupations_dict[data] = value[0]

        ad_occupations_dict[data + 1] = "अन्य"
        return Response(data=ad_occupations_dict, status=status.HTTP_200_OK)


class CasteView(APIView):
    def get(self, request, format=None):
        caste_dict = PersonsForm.CASTE.copy()
        qualifications = (
            PersonsForm.objects.all()
            .exclude(caste__in=list(caste_dict.values()))
            .values("caste")
            .distinct()
        )
        data = len(PersonsForm.CASTE)
        for value in qualifications.values_list("caste"):
            if value[0]:
                data += 1
                caste_dict[data] = value[0]
        caste_dict[data + 1] = "अन्य"
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


class InterestedOccupationListCreateView(ListCreateAPIView):
    queryset = InterestedOccupation.objects.all()
    serializer_class = InterestedOccupationsSerializer
    lookup_field = "person"


class InterestedOccupationRUDView(
    MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView
):
    queryset = InterestedOccupation.objects.all()
    serializer_class = InterestedOccupationsSerializer
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


class StatsView(TemplateView):
    template_name = "admin/survey/stats.html"
    model_admin = None

    def get_gender_report(self):
        gender = (
            PersonsForm.objects.values("gender")
            .annotate(count=Count("gender"))
            .order_by("gender")
        )
        genders_count = {1: 0, 2: 0, 3: 0}
        for key, value in gender.values_list("gender", "count"):
            genders_count[key] = value

        return genders_count

    def get_woda_report(self):
        woda = (
            PersonsForm.objects.values("permanent_address")
            .annotate(count=Count("permanent_address"))
            .order_by("permanent_address")
        )
        woda_count = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
        }

        for key, value in woda.values_list("permanent_address", "count"):
            woda_count[key] = value
        return woda_count

    def get_religion_report(self):
        religion = (
            PersonsForm.objects.values("religion")
            .annotate(count=Count("religion"))
            .order_by("-count")
        )
        religion_count = {
            "religion_name": [],
            "count": [],
        }
        others = 0
        for key, value in religion.values_list("religion", "count"):
            if key:
                religion_count["religion_name"].append(key)
                religion_count["count"].append(value)
            else:
                others += int(value)

        religion_count["religion_name"].append("अन्य")
        religion_count["count"].append(others)

        return religion_count

    def get_caste_report(self):
        caste = (
            PersonsForm.objects.values("caste")
            .annotate(count=Count("religion"))
            .order_by("-count")
        )
        caste_count = {
            "caste_name": [],
            "count": [],
        }
        others = 0
        for key, value in caste.values_list("caste", "count"):
            if key:
                caste_count["caste_name"].append(key)
                caste_count["count"].append(value)
            else:
                others += int(value)
        caste_count["caste_name"].append("अन्य")
        caste_count["count"].append(others)
        return caste_count

    def get_context_data(self, request, **kwargs):
        genders_count = self.get_gender_report()
        woda_count = self.get_woda_report()
        religion_count = self.get_religion_report()
        caste_count = self.get_caste_report()

        self.extra_context = dict(
            self.model_admin.each_context(request),
            genders_count=genders_count,
            woda_count=woda_count,
            religion_count=religion_count,
            caste_count=caste_count,
        )
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request=request, **kwargs)
        return self.render_to_response(context)
