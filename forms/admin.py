from survey.admin import admin_site
from django.contrib import admin
from django.utils.html import format_html
from forms.models import (
    PersonsForm,
    InterestedOccupation,
    PersonTrainings,
    PersonalSkills,
    Occupation,
)
import nepali_datetime


class PersonalSkillsInline(admin.TabularInline):
    model = PersonalSkills
    verbose_name = "skill"
    can_delete = False
    readonly_fields = ("skills",)


class PersonTrainingsInline(admin.TabularInline):
    model = PersonTrainings
    verbose_name = "training"
    can_delete = False
    readonly_fields = ("training",)


class EducationQualificationsInline(admin.TabularInline):
    model = InterestedOccupation
    verbose_name = "Intrested Occupation"
    can_delete = False
    readonly_fields = ("interested_occupation",)


class OccupationsInline(admin.TabularInline):
    model = Occupation
    verbose_name = "Occupation"
    can_delete = False
    readonly_fields = ("occupation",)


# Register your models here.
class PersonsFormAdmin(admin.ModelAdmin):
    model = PersonsForm
    inlines = [
        EducationQualificationsInline,
        PersonTrainingsInline,
        PersonalSkillsInline,
        OccupationsInline,
    ]
    search_fields = ("name", "citizenship", "email", "mobile_number")
    readonly_fields = ["age"]
    list_display = (
        "name",
        "gender",
        "permanent_address",
        "mobile_number",
        "birthday",
        "religion",
        "caste",
        "fathers_name",
        "mothers_name",
        "submitter_name",
        "display_photo",
    )

    def display_photo(self, obj):
        if obj.photo:
            return format_html(
                '<a href="{}"><img src="{}" width="50px" /></a>',
                obj.photo.url,
                obj.photo.url,
            )
        return "-"

    display_photo.short_description = "Photo"

    def age(self, obj):
        if obj:
            return obj.age
        return 0

    def birthday(self, obj):
        if not obj.bday:
            return "none"
        dat = nepali_datetime.date.from_datetime_date(obj.bday)
        return dat.strftime("%K-%n-%D")

    def submitter_name(self, obj):
        return str(obj.submitter.username)


admin_site.register(PersonsForm, PersonsFormAdmin)
