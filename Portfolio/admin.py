from django.contrib import admin
from Portfolio.models import Project, Contact, ProjectDetail, ProjectImage


class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']



# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDetail)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ProjectImage)

