from django.urls import path
from forms.views import (
    WodaView,
    GenderView,
    TrainingView,
    QualificationsView,
    ReligionView,
    CasteView,
    OccupationsView,
    AdmiredOccuptionView,
    PersonListCreateView,
    PersonRetrieveUpdateDeleteView,
)
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("gender/", view=GenderView.as_view(), name="list_genders"),
    path("woda/", view=WodaView.as_view(), name="list_wodas"),
    path("trainings/", view=TrainingView.as_view(), name="list_trainings"),
    path(
        "qualifications/", view=QualificationsView.as_view(), name="list_qualifications"
    ),
    path("religions/", view=ReligionView.as_view(), name="list_religions"),
    path("caste/", view=CasteView.as_view(), name="list_castes"),
    path("occupations/", view=OccupationsView.as_view(), name="list_occupations"),
    path("persons/", view=PersonListCreateView.as_view(), name="list_persons"),
    path(
        "persons/<int:pk>/",
        view=PersonRetrieveUpdateDeleteView.as_view(),
        name="update_persons",
    ),
    path(
        "admiredoccupations/",
        view=AdmiredOccuptionView.as_view(),
        name="list_admired_occupations",
    ),
    path(
        "api_schema",
        get_schema_view(title="Form schema", description="API schema for Forms"),
        name="api-schema",
    ),
    path("docs/", include_docs_urls(title="Forms API")),
]
