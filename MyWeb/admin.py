from django.contrib import admin
from .models import HomePage, AboutMe, Abilities
# Register your models here.

# this function will be used as an action in admin panel
def add_underscore_name(modeladmin, request, queryset):
    for item in queryset:
        queryset.update(name=f"__{item.name}__")

    modeladmin.message_user(request, 'items were marked by underscores successfully!')

def delete_underscores(modeladmin, request, queryset):
    for item in queryset:
        queryset.update(name=item.name[2:len(item.name) - 2])

    modeladmin.message_user(request, 'items were unmarked by underscores successfully!')



add_underscore_name.short_discription = 'Put Undersocres To Name'
delete_underscores.short_discription = 'Delete name underscores'

class AdminModel(admin.ModelAdmin):
    list_display = ('name', )
    actions = [add_underscore_name, delete_underscores]
   # list_filter = {}

admin.site.register(HomePage, AdminModel)
admin.site.register(AboutMe, AdminModel)
admin.site.register(Abilities, AdminModel)

# the above actions can be done like this

# @admin.register(HomePage)
# class AdminModel(admin.ModelAdmin):
#    list_display = ('name', )
   # list_filter = {}
