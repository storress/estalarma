from django.contrib import admin

from .models import Auto
# Register your models here.

from import_export.admin import ImportExportModelAdmin
from import_export import resources


# class AutoResource(resources.ModelResource):
#
#     class Meta:
#         model = Auto
#
#
# class AutoAdmin(ImportExportModelAdmin):
#      resource_class = AutoResource

class AutoAdmin(admin.ModelAdmin):
    fields = ['id', 'plate', 'owner', 'class_name']
    list_display = ('id', 'plate', 'owner', 'class_name')


admin.site.register(Auto, AutoAdmin)

