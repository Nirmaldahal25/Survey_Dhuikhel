from django.urls import path, include
from survey.admin import admin_site
from about import views
from about.views import AboutListCreateView,AboutRetrieveUpdateDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("about/", view = AboutListCreateView.as_view() , name="About"), 
    path(
        "about/<int:pk>/",view=AboutRetrieveUpdateDeleteView.as_view(),name="rud_persons",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)