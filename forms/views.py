from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Count
from django.http import HttpResponse
from forms.models import (
    PersonsForm,
    PersonTrainings,
    InterestedOccupation,
    PersonalSkills,
    Occupation,
)
from forms.mixins import MultipleFieldLookupMixin
from forms.serializers import (
    PersonsFormSerializer,
    InterestedOccupationsSerializer,
    PersonTrainingsSerializer,
    PersonSkillsSerializer,
    OccupationSerializer,
    LoginSerializer,
)
from django.views.generic import TemplateView
from itertools import zip_longest
import csv
import nepali_datetime
import codecs
import datetime
from django.contrib.staticfiles.storage import staticfiles_storage
import base64
import os

from django.conf import settings


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


class BloodGroupView(APIView):
    def get(self, request, format=None):
        blood_group = dict()
        for key, value in PersonsForm.BLOOD_GROUP:
            blood_group[key] = value
        return Response(data=blood_group, status=status.HTTP_200_OK)


class OccupationsView(APIView):
    def get(self, request, format=None):
        occupations_dict = Occupation.OCCUPATION.copy()
        occupations = (
            Occupation.objects.all()
            .exclude(occupation__in=list(occupations_dict.values()))
            .values("occupation")
            .distinct()
        )
        data = len(Occupation.OCCUPATION)
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


class MarriedView(APIView):
    def get(self, request, format=None):
        marriage = PersonsForm.MARRIED_STATUS
        marriage_dict = {key: value for key, value in marriage}
        return Response(data=marriage_dict, status=status.HTTP_200_OK)


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
    permission_classes = [
        IsAuthenticated,
    ]
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
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = PersonsFormSerializer
    queryset = PersonsForm.objects.all()


class InterestedOccupationListCreateView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = InterestedOccupation.objects.all()
    serializer_class = InterestedOccupationsSerializer
    lookup_field = "person"


class InterestedOccupationRUDView(
    MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView
):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = InterestedOccupation.objects.all()
    serializer_class = InterestedOccupationsSerializer
    lookup_fields = ("person", "pk")


class PersonsTrainingListCreateView(MultipleFieldLookupMixin, ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = PersonTrainings.objects.all()
    serializer_class = PersonTrainingsSerializer
    lookup_field = "person"


class PersonsTrainingRUDView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = PersonTrainings.objects.all()
    serializer_class = PersonTrainingsSerializer
    lookup_fields = ("person", "pk")


class PersonSkillListCreateView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = PersonalSkills.objects.all()
    serializer_class = PersonSkillsSerializer
    lookup_field = "person"


class PersonSkillRUDView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = PersonalSkills.objects.all()
    serializer_class = PersonSkillsSerializer
    lookup_fields = ("person", "pk")


class OccupationListCreateView(ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
    lookup_field = "person"


class OccupationRUDView(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
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
        for key, value in religion.values_list("religion", "count"):
            if key:
                religion_count["religion_name"].append(key)
                religion_count["count"].append(value)
        others = PersonsForm.objects.filter(religion=None).count()

        religion_count["religion_name"].append("अन्य")
        religion_count["count"].append(others)

        return religion_count

    def get_caste_report(self):
        caste = (
            PersonsForm.objects.values("caste")
            .annotate(count=Count("caste"))
            .order_by("-count")
        )
        caste_count = {
            "caste_name": [],
            "count": [],
        }
        for key, value in caste.values_list("caste", "count"):
            if key:
                caste_count["caste_name"].append(key)
                caste_count["count"].append(value)

        others = PersonsForm.objects.filter(caste=None).count()
        caste_count["caste_name"].append("अन्य")
        caste_count["count"].append(others)
        return caste_count

    def get_occupation_report(self):
        occupation = (
            Occupation.objects.values("occupation")
            .annotate(count=Count("occupation"))
            .order_by("-count")
        )
        occupation_count = {
            "occupation_name": [],
            "count": [],
        }
        for key, value in occupation.values_list("occupation", "count"):
            if key:
                occupation_count["occupation_name"].append(key)
                occupation_count["count"].append(value)
        return occupation_count

    def get_skills_report(self):
        skills = (
            PersonalSkills.objects.values("skills")
            .annotate(count=Count("skills"))
            .order_by("-count")
        )
        skills_count = {
            "skill_name": [],
            "count": [],
        }
        for key, value in skills.values_list("skills", "count"):
            if key:
                skills_count["skill_name"].append(key)
                skills_count["count"].append(value)
        return skills_count

    def get_training_report(self):
        trainings = (
            PersonTrainings.objects.values("training")
            .annotate(count=Count("training"))
            .order_by("-count")
        )
        trainings_count = {
            "training_name": [],
            "count": [],
        }
        for key, value in trainings.values_list("training", "count"):
            if key:
                trainings_count["training_name"].append(key)
                trainings_count["count"].append(value)
        return trainings_count

    def get_admired_occupation_report(self):
        occupation = (
            InterestedOccupation.objects.values("interested_occupation")
            .annotate(count=Count("interested_occupation"))
            .order_by("-count")
        )
        occupation_count = {
            "occupation_name": [],
            "count": [],
        }
        for key, value in occupation.values_list("interested_occupation", "count"):
            if key:
                occupation_count["occupation_name"].append(key)
                occupation_count["count"].append(value)
        return occupation_count

    def get_qualification_report(self):
        qualification = (
            PersonsForm.objects.values("qualification")
            .annotate(count=Count("qualification"))
            .order_by("-count")
        )
        qualification_count = {
            "qualification_name": [],
            "count": [],
        }
        for key, value in qualification.values_list("qualification", "count"):
            if key:
                qualification_count["qualification_name"].append(key)
                qualification_count["count"].append(value)
        return qualification_count

    def get_blood_group_report(self):
        blood_grp = (
            PersonsForm.objects.values("blood_group")
            .annotate(count=Count("blood_group"))
            .order_by("-count")
        )
        blood_grp_count = {
            "blood_group_name": [],
            "count": [],
        }
        for key, value in blood_grp.values_list("blood_group", "count"):
            if key:
                blood_grp_count["blood_group_name"].append(key)
                blood_grp_count["count"].append(value)
        return blood_grp_count

    def get_marriage_status_report(self):
        marriage_grp = (
            PersonsForm.objects.values("married")
            .annotate(count=Count("married"))
            .order_by("-count")
        )
        marriage_grp_count = {
            "marriage_group_name": [],
            "count": [],
        }
        for key, value in marriage_grp.values_list("married", "count"):
            if key:
                marriage_grp_count["marriage_group_name"].append(key)
                marriage_grp_count["count"].append(value)
        return marriage_grp_count

    def get_context_data(self, request, **kwargs):
        genders_count = self.get_gender_report()
        woda_count = self.get_woda_report()
        religion_count = self.get_religion_report()
        caste_count = self.get_caste_report()
        occupation_count = self.get_occupation_report()
        skills_count = self.get_skills_report()
        training_count = self.get_training_report()
        adoccupation_count = self.get_admired_occupation_report()
        qualification_count = self.get_qualification_report()
        blood_group_count = self.get_blood_group_report()
        marriage_count = self.get_marriage_status_report()

        self.extra_context = dict(
            self.model_admin.each_context(request),
            genders_count=genders_count,
            woda_count=woda_count,
            religion_count=religion_count,
            caste_count=caste_count,
            occupation_count=occupation_count,
            skill_count=skills_count,
            training_count=training_count,
            adoccupation_count=adoccupation_count,
            qualification_count=qualification_count,
            blood_group_count=blood_group_count,
            marriage_count=marriage_count,
        )
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request=request, **kwargs)
        return self.render_to_response(context)


class StatementView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    @staticmethod
    def get_gender(value):
        for gend in PersonsForm.GENDER:
            if value in gend:
                return gend[1]
        return PersonsForm.GENDER[0][1]

    @staticmethod
    def get_woda(value):
        for wod in PersonsForm.WODA:
            if value in wod:
                return wod[1]
        return PersonsForm.WODA[0][1]

    def generate_photo_url(self, obj):
        if obj:
            return self.request.build_absolute_uri(obj.url)
        else:
            return " "

    @staticmethod
    def nepali_date(date):
        if date:
            dat = nepali_datetime.date.from_datetime_date(date)
            return dat.strftime("%K-%n-%D")
        return " "

    def get(self, request, *args, **kwargs):
        queryset = PersonsForm.objects.all()
        headers = [
            "name",
            "gender",
            "permanent_address",
            "temporary_address",
            "email",
            "citizensip",
            "Birthday",
            "Age",
            "Fathers Name",
            "Mothers Name",
            "Religion",
            "Caste",
            "Qulification",
            "Office Domestic",
            "Office International",
            "Mobile Number",
            "Photo",
            "Occupation",
            "Trainings",
            "Skills",
            "Interested Occupation",
        ]
        response = HttpResponse(
            content_type="text/csv",
            headers={"Content-Disposition": 'attachment; filename="survey.csv"'},
        )
        response.write(codecs.BOM_UTF8)
        writer = csv.writer(response)
        writer.writerow(headers)

        for person in queryset:
            occupation = person.occupation_set.all().values_list("occupation")
            skills = person.personalskills_set.all().values_list("skills")
            training = person.persontrainings_set.all().values_list("training")
            i_occupation = person.interestedoccupation_set.all().values_list(
                "interested_occupation"
            )

            # photo_data = ""
            # if person.photo:
            #     with open(person.photo.path, "rb") as photo_file:
            #         photo_data = base64.b64encode(photo_file.read()).decode("utf-8")
            # photo_path = ""
            # if person.photo:
            #     photo_path = os.path.join(settings.MEDIA_ROOT, person.photo.name)
            photo_path = self.generate_photo_url(person.photo)

            person_list = [
                person.name,
                StatementView.get_gender(person.gender),
                StatementView.get_woda(person.permanent_address),
                person.temporary_address,
                person.email if person.email else "",
                person.citizenship if person.citizenship else "",
                StatementView.nepali_date(person.bday),
                person.age,
                person.fathers_name if person.fathers_name else "",
                person.mothers_name if person.mothers_name else "",
                person.religion if person.religion else "",
                person.caste if person.caste else "",
                person.qualification,
                person.office_domestic if person.office_domestic else "",
                person.office_international if person.office_international else "",
                person.mobile_number,
                photo_path,
            ]
            iterate = zip_longest(
                [person_list],
                list(occupation),
                list(skills),
                list(training),
                list(i_occupation),
                fillvalue="",
            )
            for info in iterate:
                row = list()
                if info[0]:
                    row = [i for i in info[0]]
                    row.extend([info[1], info[2], info[3], info[4]])
                else:
                    row = ["" for _ in range(17)]
                    other = [info[1], info[2], info[3], info[4]]
                    row.extend(other)
                writer.writerow(row)
        return response


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(
            data=self.request.data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        if not created:
            token.delete()
            token = Token.objects.create(user=user)
            token.save()
        userdict = {
            "id": user.id,
            "username": user.username,
            "name": f"{user.first_name} {user.last_name}",
            "email": user.email,
            "token": token.key,
        }
        return Response(data=userdict, status=status.HTTP_200_OK)
