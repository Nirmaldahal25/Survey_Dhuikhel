from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from forms.views import StatsView


class AdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "forms/analysis/",
                self.admin_view(StatsView.as_view(model_admin=self)),
                name="analysis",
            ),
        ]
        return my_urls + urls


admin_site = AdminSite(name="myadmin")
admin_site.register(User, UserAdmin)
