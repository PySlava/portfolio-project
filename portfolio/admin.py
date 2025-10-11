from django.contrib import admin
from .models import Project, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('tags', 'author')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'description')
        }),
        ('Метадані', {
            'fields': ('author', 'tags')
        }),
    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
