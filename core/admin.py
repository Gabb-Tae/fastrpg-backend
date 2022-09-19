from django.contrib import admin

from core.models import rpgclass, rpgrace, skills, itens, itensclass

admin.site.register(rpgclass)
admin.site.register(rpgrace)
admin.site.register(skills)
admin.site.register(itens)
admin.site.register(itensclass)