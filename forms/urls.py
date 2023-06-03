from django.urls import path
from forms.views import (
    # List Views
    WodaView,
    GenderView,
    TrainingView,
    QualificationsView,
    ReligionView,
    CasteView,
    OccupationsView,
    AdmiredOccuptionView,
    PersonalSkillsView,
    StatementView,
    BloodGroupView,
    MarriedView,
    # Person Views
    PersonListCreateView,
    PersonRetrieveUpdateDeleteView,
    # List Create Views
    PersonsTrainingListCreateView,
    InterestedOccupationListCreateView,
    PersonSkillListCreateView,
    OccupationListCreateView,
    # Retrieve Update Delete Views
    InterestedOccupationRUDView,
    PersonSkillRUDView,
    PersonsTrainingRUDView,
    OccupationRUDView,
    # Get User
    LoginView,
)

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("list/gender/", view=GenderView.as_view(), name="list_genders"),
    path("list/woda/", view=WodaView.as_view(), name="list_wodas"),
    path("list/trainings/", view=TrainingView.as_view(), name="list_trainings"),
    path(
        "list/qualifications/",
        view=QualificationsView.as_view(),
        name="list_qualifications",
    ),
    path("list/religions/", view=ReligionView.as_view(), name="list_religions"),
    path("list/castes/", view=CasteView.as_view(), name="list_castes"),
    path("list/occupations/", view=OccupationsView.as_view(), name="list_occupations"),
    path("list/skills/", view=PersonalSkillsView.as_view(), name="list_skills"),
    path("list/bloodgroups/", view=BloodGroupView.as_view(), name="list_blood_groups"),
    path("list/marriage/", view=MarriedView.as_view(), name="list_married_stats"),
    path(
        "list/admiredoccupations/",
        view=AdmiredOccuptionView.as_view(),
        name="list_admired_occupations",
    ),
    path("user/login/", view=LoginView.as_view(), name="get_user_id"),
    path(
        "persons/<int:person>/admiredoccupations/<int:pk>/",
        view=InterestedOccupationRUDView.as_view(),
        name="rud_person_interested_occupations",
    ),
    path(
        "persons/<int:person>/skills/<int:pk>/",
        view=PersonSkillRUDView.as_view(),
        name="rud_person_skills",
    ),
    path(
        "persons/<int:person>/trainings/<int:pk>/",
        view=PersonsTrainingRUDView.as_view(),
        name="rud_person_trainings",
    ),
    path(
        "persons/<int:person>/occupations/<int:pk>/",
        view=OccupationRUDView.as_view(),
        name="rud_person_occupations",
    ),
    path(
        "persons/<int:person>/admiredoccupations/",
        view=InterestedOccupationListCreateView.as_view(),
        name="list_person_interested_occupations",
    ),
    path(
        "persons/<int:person>/occupations/",
        view=OccupationListCreateView.as_view(),
        name="list_person_occupations",
    ),
    path(
        "persons/<int:person>/skills/",
        view=PersonSkillListCreateView.as_view(),
        name="list_person_skills",
    ),
    path(
        "persons/<int:person>/trainings/",
        view=PersonsTrainingListCreateView.as_view(),
        name="list_persons_training",
    ),
    path(
        "persons/<int:pk>/",
        view=PersonRetrieveUpdateDeleteView.as_view(),
        name="rud_persons",
    ),
    path("persons/", view=PersonListCreateView.as_view(), name="list_persons"),
    path("statement/", view=StatementView.as_view(), name="download_survey_report"),
    path(
        "api_schema",
        get_schema_view(title="Form schema", description="API schema for Forms"),
        name="api-schema",
    ),
    path("docs/", include_docs_urls(title="Forms API")),
]
