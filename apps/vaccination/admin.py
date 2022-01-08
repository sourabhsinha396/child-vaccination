from django.contrib import admin
from .models import ContactUs, Parent, Mother, Child, Vaccine, ChildVaccinated, MotherVaccinated


admin.site.register(ContactUs) 
admin.site.register(Parent) 
admin.site.register(Mother) 
admin.site.register(Child)
admin.site.register(ChildVaccinated)
admin.site.register(MotherVaccinated)


class VaccinationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Vaccine, VaccinationAdmin)
