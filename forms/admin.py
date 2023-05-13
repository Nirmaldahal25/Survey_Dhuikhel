from django.contrib import admin
from forms.models import (
    PersonsForm,
    EducationQualifications,
    PersonTrainings,
    PersonalSkills,
)


class PersonalSkillsInline(admin.TabularInline):
    model = PersonalSkills
    verbose_name = "skill"
    can_delete = False


class PersonTrainingsInline(admin.TabularInline):
    model = PersonTrainings
    verbose_name = "training"
    can_delete = False


class EducationQualificationsInline(admin.TabularInline):
    model = EducationQualifications
    verbose_name = "qualification"
    can_delete = False


# Register your models here.
class PersonsFormAdmin(admin.ModelAdmin):
    model = PersonsForm
    inlines = [
        EducationQualificationsInline,
        PersonTrainingsInline,
        PersonalSkillsInline,
    ]


admin.site.register(PersonsForm, PersonsFormAdmin)
