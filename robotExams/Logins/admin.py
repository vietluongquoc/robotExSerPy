from django.contrib import admin
from django.contrib.auth.models import User
from .models import examDb, questionDb
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

            
class questionDbResource(resources.ModelResource):
    class Meta:
        model = questionDb
        import_id_fields = ('questiontype', 'questionText', 'ispicture', 'picture', 'optionA', 'optionB', 'optionC', 'optionD', 'correctAnswer')
        exclude = ('id')

class examDbResource(resources.ModelResource):
    class Meta:
        model = examDb
        import_id_fields = ('user', 'device_id', 'questionArray', 'answerArray')
        exclude = ('id')

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('id','username','password', 'email', 'first_name', 'last_name', 'is_staff')


@admin.register(examDb)
class examDbAdmin(ImportExportModelAdmin):
    resource_class = examDbResource
    list_display = ('user', 'device_id','questionArray', 'answerArray')

@admin.register(questionDb)
class questionDbAdmin(ImportExportModelAdmin):
    resource_class = questionDbResource
    list_display = ('id', 'questiontype', 'questionText', 'ispicture', 'picture', 'optionA', 'optionB', 'optionC', 'optionD', 'correctAnswer')