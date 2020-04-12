from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ( UserSelect )

# Register your models here.

@admin.register(UserSelect)
class UserSelectAdmin(ImportExportModelAdmin):
    list_display = ('id', 'selected')
    list_display_links = ('id', )
    list_filter = ('selected',)