from django.contrib import admin
from .models import Project, User

# Register your models here.
class MemberAdminInline(admin.TabularInline):
    model = User

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'admin_image')
    inlines = (MemberAdminInline, )


admin.site.register(Project, ProjectAdmin)
admin.site.register(User)