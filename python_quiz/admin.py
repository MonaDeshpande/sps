from django.contrib import admin
from .models import administrator_login

# Register your models here.
class administratorAdmin(admin.ModelAdmin):
    list_display= ('firstname', 'lastname', 'admin_id')
    list_editable= ('lastname', 'admin_id')


admin.site.register(administrator_login, administratorAdmin)


