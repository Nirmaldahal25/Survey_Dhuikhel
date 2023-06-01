from django.contrib import admin
from about.models import About
from survey.admin import admin_site

class AboutFormAdmin(admin.ModelAdmin):
    model = About
    search_fields = ("name","mobile_number","email")
    list_display = (
        "name",
        "position",
        "mobile_number",
        "email",
        "address",
    )

# admin_site.register(PersonsForm, PersonsFormAdmin)
# Register your models here.
admin_site.register(About,AboutFormAdmin)