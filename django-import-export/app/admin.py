#admin.py
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin, ExportActionMixin
from import_export import resources
from app.models import Member
from app.resources import MemberResource


# @admin.register(Member)
# class MemberAdmin(ImportExportModelAdmin):
#     list_display = ("firstname", "lastname", "email", "birth_date")
    
class MemberAdminAction(ImportExportModelAdmin, ExportActionMixin, admin.ModelAdmin):
    resource_class=MemberResource
    list_display = ("firstname", "lastname", "email", "birth_date")
    
admin.site.register(Member, MemberAdminAction)