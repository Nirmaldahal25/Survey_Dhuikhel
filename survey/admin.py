from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class AdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                "forms/analysis/",
                self.admin_view(self.stastics_view),
                name="analysis",
            )
        ]
        return my_urls + urls

    def stastics_view(self, request, *args, **kwargs):
        context = dict(self.each_context(request), user=request.user)
        return TemplateResponse(request, "admin/survey/stats.html", context)


admin_site = AdminSite(name="myadmin")
admin_site.register(User, UserAdmin)
