from django.contrib import admin
from forms.models import (
    PersonsForm,
    EducationQualifications,
    PersonTrainings,
    PersonalSkills,
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
    model = EducationQualifications
    verbose_name = "qualification"
    can_delete = False
    readonly_fields = ("qualification",)


# Register your models here.
class PersonsFormAdmin(admin.ModelAdmin):
    model = PersonsForm
    inlines = [
        EducationQualificationsInline,
        PersonTrainingsInline,
        PersonalSkillsInline,
    ]
    search_fields = ("name", "citizenship", "email", "mobile_number")
    readonly_fields = ["age"]
    list_display = ("name", "mobile_number", "citizenship", "birthday")

    def age(self, obj):
        if obj:
            return obj.age
        return 0

    def birthday(self, obj):
        dat = nepali_datetime.date.from_datetime_date(obj.bday)
        return dat.strftime("%K-%n-%D")


admin.site.register(PersonsForm, PersonsFormAdmin)
