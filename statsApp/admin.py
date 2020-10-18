from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Stats


@admin.register(Stats)
class ViewAdmin(ImportExportModelAdmin):
    pass
