from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import itens, rpgclass, rpgrace, skills, zcharacter
from core.models.usuario import Usuario


class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "school_class", "birth_date")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(rpgclass)
admin.site.register(rpgrace)
admin.site.register(skills)
admin.site.register(itens)
admin.site.register(zcharacter)

class itensAdmin(admin.ModelAdmin):
    list_display = ('name', 'definition')
    search_fields = ('name', 'definition')
    list_filter = ('name')
    ordering = ('name')

class rpgclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)

class rpgraceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name')
    ordering = ('name')
    
class skillsAdmin(admin.ModelAdmin):
    list_display = ('description')
    search_fields = ('description')
    list_filter = ('description')
    ordering = ('description')

class zcharacterAdmin(admin.ModelAdmin):
    list_display = ('nome')
    search_fields = ('name')
    list_filter = ('name')
    ordering = ('name')