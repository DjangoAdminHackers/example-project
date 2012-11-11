from django.contrib import admin
from models import Club, Member

class MemberInline(admin.TabularInline):
    model = Member
    extra = 1

class ClubAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    ordering = ('-name',)
    list_per_page = 10
    inlines = [MemberInline,]

class MemberAdmin(admin.ModelAdmin):
    list_display = ('fname', 'sname', 'club',)
    list_display_links = ('fname', 'sname',)
    list_filter = ('club',)
    list_editable = ('club',)
    search_fields = ('fname', 'sname',)
    ordering = ('-sname',)
    list_per_page = 10

admin.site.register(Club, ClubAdmin)
admin.site.register(Member, MemberAdmin)
