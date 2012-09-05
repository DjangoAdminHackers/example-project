from django.contrib import admin
from models import Company, Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'comany',)
    list_display_links = ('first_name', 'last_name',)
    list_filter = ('comany',)
    list_editable = ('comany',)
    search_fields = ('first_name', 'last_name',)
    ordering = ('-last_name',)
    list_per_page = 10  

admin.site.register(Company)
admin.site.register(Person, PersonAdmin)
