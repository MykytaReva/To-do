from django.contrib import admin
from todo.models import ToDo
from rangefilter.filters import DateTimeRangeFilter

from import_export.admin import ImportExportModelAdmin
from import_export import resources




class ToDoResource(resources.ModelResource):

    class Meta:
        model = ToDo
        fields = (
            'id',
            'subject',
            'date_todo',
            'when',
            'status',
        )
        export_order = (
            'id',
            'subject',
            'date_todo',
            'when',
            'status',
        )


class ToDoAdmin(ImportExportModelAdmin):
    model = ToDo
    resource_class = ToDoResource
    list_display = (
        'id',
        'subject',
        'date_todo',
        'status',
    )
    readonly_fields = (
        'id',
        'subject',
        'date_todo',
        'status',
    )


    search_fields = (
        'status',
        'subject',
    )

    list_filter = (
        'status',
        ('when', DateTimeRangeFilter)
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_create_permission(self, request, obj=None):
        return False





# class ToDoAdmin(ImportExportModelAdmin, admin.ModelAdmin)):
#     resource_class = ToDoResource



admin.site.register(ToDo, ToDoAdmin)