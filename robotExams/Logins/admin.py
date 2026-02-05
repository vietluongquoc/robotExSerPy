from django.contrib import admin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.hashers import make_password


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ('username', 'password', 'email', 'first_name', 'last_name', 'is_staff')
        exclude = ('id') 
    
    def before_import_row(self, row, **kwargs):
        if 'password' in row:
            row['password'] = make_password(row['password'])

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('id','username','password', 'email', 'first_name', 'last_name', 'is_staff')